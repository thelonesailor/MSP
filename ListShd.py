import sys
from heapq import heappush,heappop,heapify
cin = sys.stdin
cout = sys.stdout
def find_schedule(graph,p,time):
	schedule = [[] for i in xrange(p)]
	child = graph[0]
	parent = graph[1]
	n = len(time)
	ls = [(time[i],i) for i in xrange(n)]
	ls.sort(key=lambda x:x[0],reverse=True)
	ls = [elem[1] for elem in ls]
	done = [0]*n
	end_time = [-99]*n
	donect=0 
	heap = [(0,i) for i in xrange(p)]
	heapify(heap)
	while donect<n :
		item = heappop(heap)
		tproc = item[0]
		proc = item[1]
		lefttask = -1
		for task in ls:
			if done[task]:
				continue
			flag=True
			for par in parent[task]:
				if end_time[par]<0 or end_time[par]>tproc:
					flag=False
					break
			if flag:
				lefttask=task
				break
		if lefttask!=-1:
			heappush(heap,(tproc+time[lefttask],proc))
			schedule[proc].append(lefttask)
			donect+=1
			done[lefttask]=1
			end_time[lefttask]=tproc+time[lefttask]
		else:
			tmp = []
			while heap and heap[0][0]==tproc:
				tmp.append(heappop(heap))
			new_time = heap[0][0]
			while tmp:
				heappush(heap,(new_time,(tmp.pop())[1]))
	mtime = max(elem[0] for elem in heap)
	return schedule,mtime

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

def sanity_check(schedule,num_tasks):
	sm = sum(len(processor) for processor in schedule)
	if sm!=num_tasks:
		print "Net tasks not preserved"

num_tasks,num_edges,num_proc, = map(int,cin.readline().split(' '))
time = map(int,cin.readline().split(' '))
graph = [[] for i in xrange(num_tasks)],[[] for i in xrange(num_tasks)]
for i in xrange(num_edges):
	a,b = map(int,cin.readline().split(' '))
	graph[0][a].append(b)
	graph[1][b].append(a)
result = find_schedule(graph,num_proc,time)
schedule = result[0]
sanity_check(schedule,num_tasks)
for proc in schedule:
	print [task for task in proc]
print finish_time(graph,schedule,time),result[1]

