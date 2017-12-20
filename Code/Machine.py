import sys,random,bisect
from heapq import heappush,heappop
cin = sys.stdin
cout = sys.stdout
def cal_height(graph):
	n = len(graph[0])
	ht = [-1 for i in xrange(n)]
	child = graph[0]
	parent = graph[1]	
	for i in xrange(n):
		if ht[i]==-1:
			S = [i]
			while S:
				nd = S[-1]
				if ht[nd]!=-1:
					S.pop()
					ht[nd] = (max([ht[par] for par in parent[nd]] or [-1]))+1
				else:
					ht[nd]=0
					S.extend([par for par in parent[nd] if ht[par]==-1])
	#print "Heigth:",ht
	mht = max(ht)
	newht = []
	for i in xrange(n):
		minval = min([ht[chd] for chd in child[i]] or [mht+1])-1
		newht.append(random.randint(ht[i],minval))
	return newht

def search_task(schedule,task):
	for i in xrange(len(schedule)):
		for j in xrange(len(schedule[i])):
			if schedule[i][j]==task:
				return i,j
	print "Searching for the wrong task in the schedule"
	return 0,0

def finish_time(graph,schedule,time):
	n = len(graph[0])
	parent = graph[1]
	pos = [(-1,-1) for i in xrange(n)]
	for i in xrange(len(schedule)) :
		for j in xrange(len(schedule[i])) :
			pos[schedule[i][j]]=(i,j)
	for elem in pos :
		if elem==(-1,-1):
			print "Repeat Error"			
	time_tasks = [-1]*n
	for i in xrange(n):
		if time_tasks[i]==-1:
			S = []
			S.append(i)
			while S :
				task = S[-1]
				x,y = pos[task]
				ptask = schedule[x][y-1] if y else -1 		
				if time_tasks[task]!=-1:
					S.pop()
					min_par = max([time_tasks[par] for par in parent[task]] or [0])
					minimum = min_par if y==0 else max(min_par,time_tasks[ptask])
					time_tasks[task] = time[task]+minimum
				else:
					time_tasks[task]=0
					if y:
						S.append(ptask)
					for par in parent[task]:
						if time_tasks[par]==-1 and par!=ptask:
							S.append(par)
	return max(time_tasks)

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

def crossover(s1,s2,hg):
	num_procs = len(s1)
	max_height = max(hg)
	c = random.randint(0,max_height)
	ls1 = [([nd for nd in s1[i] if hg[nd]<=c]+[nd for nd in s2[i] if hg[nd]>c]) for i in xrange(num_procs)]
	ls2 = [([nd for nd in s2[i] if hg[nd]<=c]+[nd for nd in s1[i] if hg[nd]>c]) for i in xrange(num_procs)]
	return (ls1,ls2)

def generate_schedule(tasksets,num_proc,num_tasks):
	schedule = [[] for i in xrange(num_proc)]
	for tset in tasksets:
		procs = range(num_proc)
		random.shuffle(tset)
		random.shuffle(procs)
		for i in xrange(num_proc-1):
			r = random.randint(0,len(tset))
			schedule[procs[i]].extend(tset[-r:])
			tset = tset[:-r]
		schedule[procs[-1]].extend(tset)
	return schedule

def generate_task_set(num_tasks,height):
	tasksets = [[] for i in xrange(max(height)+1)]
	for i in xrange(num_tasks):
		tasksets[height[i]].append(i)
	return tasksets

def reproduction(schedules,fit_val):
	num_schedule = len(schedules)
	fit_sum = sum(fit_val)
	wheel = []
	sm=0
	for i in xrange(num_schedule):
		sm+=fit_val[i]
		wheel.append(sm)
	new_schedules = []
	for i in xrange(num_schedule):
		selection = random.randint(1,fit_sum)
		selected_index = bisect.bisect_left(wheel,selection)
		new_schedules.append(schedules[selected_index])
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
			print "Net tasks not preserved"
		for processor in schedule:
			for i in xrange(len(processor)-1):
				if height[processor[i]]>height[processor[i+1]]:
					print "Height Ordering Not followed"

def find_schedule(graph,num_proc,time,pop_size,num_iterations):
	#print time
	num_tasks = len(graph[0])
	height = cal_height(graph)
	#print "Height\':",height
	tasksets = generate_task_set(num_tasks,height)
	schedules = [generate_schedule(tasksets,num_proc,num_tasks) for i in xrange(pop_size)]
	iterations = 0
	ftime = [finish_time(graph,schedule,time) for schedule in schedules]
	while iterations!=num_iterations:
		sanity_check(schedules,height)
		maxtime,mintime = max(ftime),min(ftime)
		fit_val = [(maxtime-times)+1 for times in ftime]
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
		best_time = finish_time(graph,best_shd,time)
		ftime = [finish_time(graph,schedule,time) for schedule in schedules]
		mxi = ftime.index(max(ftime))
		schedules[mxi]=best_shd
		ftime[mxi]=best_time
		iterations+=1

	# print best_time
	cout.write(str(best_time)+"\n")
	# fd=open("result.txt",'a')	
	# fd.write(str(best_time)+",")
	# fd.close()
	# print best_shd

# Input Format: On the first line there are three integers which are number of processors,number of tasks,
# number of edges in the task graph respectively.
# line consisting of num_tasks numbers
# then num of edges lines follow each of which contains two integers u,v denoting edge is from u to v.
num_tasks,num_edges,num_proc, = map(int,cin.readline().split(' '))
time = map(int,cin.readline().split(' '))
graph = [[] for i in xrange(num_tasks)],[[] for i in xrange(num_tasks)]
for i in xrange(num_edges):
	a,b = map(int,cin.readline().split(' '))
	graph[0][a].append(b)
	graph[1][b].append(a)
find_schedule(graph,num_proc,time,500,100)
