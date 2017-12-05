import sys
from random import shuffle
from heapq import heappush,heappop,heapify
cin = sys.stdin
cout = sys.stdout
def find_schedule(graph,p,ls):
	schedule = [[] for i in xrange(p)]
	child = graph[0]
	parent = graph[1]
	n = len(time)
	# ls = [(time[i],i) for i in xrange(n)]
	# ls.sort(key=lambda x:x[0],reverse=True)

	# ls = [elem[1] for elem in ls]
	
		
	done = [False]*n
	end_time = [-1]*n
	donect=0 
	heap = [(0,i) for i in xrange(p)]
	heapify(heap)
	while donect<n :
		item = heappop(heap)
		tproc = item[0]
		proc = item[1]
		lefttask = -1
		for i in xrange(len(ls)):
			task=ls[i]
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
			done[lefttask]=True
			end_time[lefttask]=tproc+time[lefttask]
		else:
			tmp = []
			while heap and heap[0][0]==tproc:
				tmp.append(heappop(heap))
			new_time = heap[0][0]
			# new_time = tproc+1
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

n=len(time)
assert n==num_tasks

h=[-1 for i in range(0,n)]
pred=graph[1]
succ=graph[0]


def height(t):
	global h
	if(h[t]>-1):
		return h[t]

	if(pred[t]==[]):
		h[t]=0
	else:
		maxh=-1
		for a in pred[t]:
			temp=height(a)
			if(temp>maxh):
				maxh=temp

		if(maxh==-1):
			print("something is wrong 1")

		h[t]=maxh+1

	return h[t]

for i in range(0,n):
	height(i)
	if(h[i]==-1):
		print("Something Wrong for h["+str(i)+"]  2")

# num_proc=3

ls = [(time[i],i) for i in xrange(n)]
ls.sort(key=lambda x:x[0],reverse=False)	
ls2=[]
for i in range(len(ls)):
	ls2.append(ls[i][1])
ls=ls2
result = find_schedule(graph,num_proc,ls)
schedule = result[0]
sanity_check(schedule,num_tasks)
print "Increasing order of time"
# for proc in schedule:
# 	print [task for task in proc]
print finish_time(graph,schedule,time),result[1]


ls = [(time[i],i) for i in xrange(n)]
ls.sort(key=lambda x:x[0],reverse=True)	
ls2=[]
for i in range(len(ls)):
	ls2.append(ls[i][1])
ls=ls2
result = find_schedule(graph,num_proc,ls)
schedule = result[0]
sanity_check(schedule,num_tasks)
print "Decreasing order of time"	
# for proc in schedule:
	# print [task for task in proc]
print finish_time(graph,schedule,time),result[1]



bestschedule=schedule
besttime=result[1]

worstschedule=schedule
worsttime=result[1]

# try some random permutations
for i in xrange(10000):
	ls = [i for i in xrange(n)]
	shuffle(ls)
	shuffle(ls)

	# print(ls)	
	result = find_schedule(graph,num_proc,ls)
	schedule = result[0]
	sanity_check(schedule,num_tasks)
	# for proc in schedule:
	# 	print [task for task in proc]
	temp=finish_time(graph,schedule,time)
	# print(temp)
	assert temp==result[1]
	# print temp,result[1]
	if(result[1]<besttime):
		besttime=result[1]
		bestschedule=schedule

	if(result[1]>worsttime):
		worsttime=result[1]
		worstschedule=schedule

print("Result of random permutations")
# for proc in bestschedule:
# 	print [task for task in proc]
print "Best="+str(besttime)

# for proc in worstschedule:
# 	print [task for task in proc]
print "Worst="+str(worsttime)

# print float(worsttime)/besttime,2.0-1.0/num_proc


# try topological sort
roots=[]
for i in range(n):
	if(pred[i]==[]):
		roots.append(i)

bs=[]
bt=1000000000
wt=0
ws=[]
# TODO: permute roots
for num in range(1000):
	shuffle(roots)
	topo=[]
	tk=0
	taken=[0 for i in range(n)]
	for i in range(len(roots)):
		topo.append(roots[i])
		taken[roots[i]]=1
		tk+=1

	while(tk<n):
		poss=[]
		for i in range(n):
			temp=0
			if(taken[i]==1):
				continue
			for j in pred[i]:
				if(taken[j]==1):
					temp+=1
			if(temp==len(pred[i])):		
				poss.append(i)	
		dis=0
		di=-1		
		order=[]
		for i in range(len(poss)):
			a=poss[i]
			mind=0
			distances=[]
			for j in range(len(topo)):
				if(topo[j] in pred[a]):
					mind=max(mind,j)
					distances.append(len(topo)-j)
			distances.sort()
			order.append((distances,poss[i]))
			if(mind>dis):
				dis=mind
				di=i

		order.sort(reverse=True)
		take=order[0][1]		
		topo.append(take)
		taken[take]=1	
		tk+=1	

	# print topo
	result = find_schedule(graph,num_proc,topo)
	schedule = result[0]
	if(result[1]<bt):
		bt=result[1]
		bs=schedule
	if(result[1]>wt):
		wt=result[1]
		ws=schedule
		
	sanity_check(schedule,num_tasks)
	# for proc in schedule:
	# 	print [task for task in proc]
	assert finish_time(graph,schedule,time)==result[1]


print "Result of Topological sorts"
# for proc in bs:
# 	print [task for task in proc]
print "Best="+str(bt)

# for proc in ws:
# 	print [task for task in proc]
print "Worst="+str(wt)
					