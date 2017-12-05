import sys,random
from heapq import heappush,heappop
cin = sys.stdin
cout = sys.stdout
def cal_height(graph):
	n = len(graph)
	ht = [-1 for i in xrange(n)]
	for i in xrange(n):
		if ht[i]==-1:
			S = []
			S.append(i)
			while S:
				nd = S[-1]
				if ht[nd]!=-1:
					S.pop()
					ht[nd] = (max([ht[par] for par in xrange(n) if graph[par][nd]==1] or [-1]))+1
				else:
					ht[nd]=0
					S.extend([par for par in xrange(n) if graph[par][nd]==1 and ht[par]==-1])
	print "Heigth:",ht
	return ht
	newht = []
	for i in xrange(n):
		cheights = [ht[chd] for chd in xrange(n) if graph[i][chd]==1]
		minval = (min(cheights) if cheights else 10)-1
		newht.append(random.randint(ht[i],minval))
	return newht

def search_task(schedule,task):
	for i in xrange(len(schedule)):
		for j in xrange(len(schedule[i])):
			if schedule[i][j]==task:
				return i,j
	return 0,0

def mutation(schedule,height):
	n = len(schedule)
	task1 = random.randint(0,n-1)
	candidates = [elem for elem in xrange(n) if height[elem]==height[task1] and elem!=task1]
	if not candidates :
		return
	task2 = random.choice(candidates)
	i1,j1 = search_task(schedule,task1)
	i2,j2 = search_task(schedule,task2)
	schedule[i1][j1],schedule[i2][j2] = schedule[i2][j2],schedule[i1][j1]

def finish_time(graph,schedule,len_tasks):
	n = len(graph)
	pos = [(-1,-1) for i in xrange(n)]
	for i in xrange(len(schedule)) :
		for j in xrange(len(schedule[i])) :
			#print "Schedule:",schedule[i][j]
			pos[schedule[i][j]]=(i,j)
	for elem in pos :
		if elem==(-1,-1):
			print "Repeat Error"			
	time_tasks = [-1]*n
	for i in xrange(n):
		if time_tasks[i]==-1:
			S = []
			S.append(i)
			ct=0
			while S :			
				task = S[-1]
				x,y = pos[task]					
				if time_tasks[task]!=-1:
					S.pop()
					min_par = max([time_tasks[par] for par in xrange(n) if graph[par][task]==1] or [0])
					time_tasks[task] = len_tasks[task]+(min_par if y==0 else max(min_par,time_tasks[schedule[x][y-1]]))
				else:
					time_tasks[task]=0
					if y and graph[schedule[x][y-1]][task]!=1:
						S.append(schedule[x][y-1])
					S.extend([par for par in xrange(n) if graph[par][task]==1 and time_tasks[par]==-1])

	return max(time_tasks)

def crossover(schedule1,schedule2,height):
	num_procs = len(schedule1)
	max_height = max(height)
	c = random.randint(0,max_height)
	list1,list2 = [],[]
	for i in xrange(num_procs):
		ls = [elem for elem in schedule1[i] if height[elem]<=c]
		ls.extend([elem for elem in schedule2[i] if height[elem]>c])
		list1.append(ls)
		ls = [elem for elem in schedule2[i] if height[elem]<=c]
		ls.extend([elem for elem in schedule1[i] if height[elem]>c])
		list2.append(ls)
	return (list1,list2)

def generate_schedule(tasksets,num_proc,num_tasks):
	schedule = [[] for i in xrange(num_proc)]
	for tset in tasksets:
		procs = range(num_proc)
		random.shuffle(procs)
		for i in xrange(num_proc-1):
			r = random.randint(0,len(tset))
			schedule[procs[i]].extend(tset[-r:])
			tset = tset[:-r]
		schedule[procs[-1]].extend(tset)
	return schedule

def generate_task_set(num_tasks,height):
	mht = max(height)
	tasksets = [[] for i in xrange(mht+1)]
	for i in xrange(num_tasks):
		tasksets[height[i]].append(i)
	return tasksets

def reproduction(schedules,fit_val):
	num_schedule = len(schedules)
	fit_sum = sum(fit_val)
	wheel = []
	for i in xrange(num_schedule):
		for j in xrange(fit_val[i]):
			wheel.append(i)
	new_schedules = []
	for i in xrange(num_schedule):
		selection = random.randint(0,fit_sum-1)
		new_schedules.append(schedules[wheel[selection]])
	return new_schedules

def pop_schedule(schedules):
	elem_idx = random.randint(0,len(schedules)-1)
	schedules[-1],schedules[elem_idx] = schedules[elem_idx],schedules[-1]
	return schedules.pop()

def print_Schedules(schedules,ftime):
	for ith,schedule in enumerate(schedules) :
		print "Finish Time of",ith,"Schedule:",ftime[ith]	
		for j,processor in enumerate(schedule):
			print "Processor",j,":",[elem+1 for elem in processor]
	print "\n\n"

def sanity_check(schedules,height):
	for schedule in schedules:
		sm = sum(len(processor) for processor in schedule)
		if sm!=len(height):
			print "Error"
		for processor in schedule:
			for i in xrange(len(processor)-1):
				if height[processor[i]]>height[processor[i+1]]:
					print "Error"

def find_schedule(graph,num_proc,pop_size,len_tasks):
	print len_tasks
	num_tasks = len(graph)
	height = cal_height(graph)
	print "Height\':",height
	tasksets = generate_task_set(num_tasks,height)
	schedules = []
	for i in xrange(pop_size):
		schedules.append(generate_schedule(tasksets,num_proc,num_tasks))
	iterations = 0
	while iterations!=100:
		ftime = [finish_time(graph,schedule,len_tasks) for schedule in schedules]
		#print "Iteration:",iterations
		#print_Schedules(schedules,ftime)
		sanity_check(schedules,height)
		maxtime,mintime = max(ftime),min(ftime)
		fit_val = [(maxtime-time)+1 for time in ftime]
		best_shd = schedules[ftime.index(mintime)]
		new_schedules = reproduction(schedules,fit_val)
		tmp_schedules = []
		for i in xrange(pop_size/2):
			schedule1 = pop_schedule(new_schedules)
			schedule2 = pop_schedule(new_schedules)
			schedule1,schedule2 = crossover(schedule1,schedule2,height)
			tmp_schedules.append(schedule1)
			tmp_schedules.append(schedule2)
		schedules = []
		for schedule in tmp_schedules:
			selection = random.randint(1,20)
			if selection==1:
				mutation(schedule,height)
			schedules.append(schedule)
		ftime = [finish_time(graph,schedule,len_tasks) for schedule in schedules]
		schedules[ftime.index(min(ftime))]=best_shd
		iterations+=1
		print finish_time(graph,best_shd,len_tasks)
	# print finish_time(graph,[[21, 18, 5, 22, 25, 26, 32, 39, 9, 15, 16, 23], [35, 8, 10, 12, 37, 11, 24, 38], [27, 28, 30, 31, 7, 20, 29, 34, 36, 13], [0, 19, 14], [1, 2, 17, 4, 6, 33, 3]],len_tasks)
	
	print best_shd


# Input Format: On the first line there are three integers which are number of processors,number of tasks,
# number of edges in the task graph respectively.
# line consisting of num_tasks numbers
# then num of edges lines follow each of which contains two integers u,v denoting edge is from u to v.
num_tasks,num_edges,num_proc, = map(int,cin.readline().split(' '))
len_tasks = map(int,cin.readline().split(' '))
graph = [[0 for i in xrange(num_tasks)] for i in xrange(num_tasks)]
for i in xrange(num_edges):
	a,b = map(int,cin.readline().split(' '))
	graph[a][b]=1
#print graph
#for i in xrange(num_tasks):
#	print "Child",i,":",[chd for chd in xrange(num_tasks) if graph[i][chd]==1]
#	print "Parent",i,":",[par for par in xrange(num_tasks) if graph[par][i]==1]
find_schedule(graph,num_proc,500,len_tasks)
