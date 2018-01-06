import sys
from random import shuffle
from heapq import heappush, heappop, heapify
cin = sys.stdin
cout = sys.stdout


def find_schedule(graph, p, ls):
	schedule = [[] for i in range(p)]
	child = succ
	parent = pred
	# n = len(time)

	done = [False]*n
	end_time = [-1]*n
	donect=0
	heap = [(0,i) for i in range(p)]
	heapify(heap)
	while donect < n:
		item = heappop(heap)
		tproc = item[0]
		proc = item[1]
		lefttask = -1
		for i in range(n):
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
			if(heap):
				new_time = heap[0][0]
			else:
				new_time = tproc+1
			while tmp:
				heappush(heap,(new_time,(tmp.pop())[1]))
			heappush(heap,(new_time,proc))

	mtime = max(elem[0] for elem in heap)
	return schedule,mtime

def finish_time(graph,schedule,time):

	pos = [(-1,-1) for i in range(n)]
	for i in range(len(schedule)) :
		for j in range(len(schedule[i])) :
			pos[schedule[i][j]]=(i,j)
	for elem in pos :
		assert elem!=(-1,-1)

	time_tasks = [-1]*n
	for i in range(n):
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

def sanity_check(schedule,num_tasks,res_time):
	sm = sum(len(processor) for processor in schedule)
	assert sm==num_tasks
	pos = [(-1,-1) for i in range(num_tasks)]
	for i in range(len(schedule)) :
		for j in range(len(schedule[i])) :
			pos[schedule[i][j]]=(i,j)
	for elem in pos :
		assert elem!=(-1,-1)
	for proc in schedule:
		for i in range(0,len(proc)):
			task = proc[i]
			pari = pred[task]
			for j in range(i+1,len(proc)):
				task2 = proc[j]
				assert task2 not in pari
	assert finish_time(graph,schedule,time)==res_time




num_tasks,num_edges,num_proc, = map(int,cin.readline().split(' '))
time = list(map(int,cin.readline().split(' ')))

n=len(time)
assert n==num_tasks

graph=[[0 for j in range(n)] for i in range(n)]
pred = [[] for i in range(n)]
succ = [[] for i in range(n)]
for i in range(num_edges):
	a,b = map(int,cin.readline().split(' '))
	graph[a][b]=1


for k in range(n):
	for i in range(n):
		for j in range(n):
			if graph[i][k] and graph[k][j] :
				graph[i][j]=1


for i in range(n):
	for j in range(n):
		if graph[i][j] :
			for k in range(n):
				if graph[j][k]:
					graph[i][k]=0

for i in range(n):
	for j in range(n):
		if graph[i][j]:
			succ[i].append(j)
			pred[j].append(i)

parent=pred
child=succ


## Increasing order of time
ls = [(time[i],i) for i in range(n)]
ls.sort(key=lambda x:x[0],reverse=False)
ls2=[]
for i in range(len(ls)):
	ls2.append(ls[i][1])
ls=ls2
result = find_schedule(graph,num_proc,ls)
schedule = result[0]
# sanity_check(schedule,num_tasks)
# print ("Increasing order of time")
# for proc in schedule:
# 	print [task for task in proc]
# assert finish_time(graph,schedule,time)==result[1]
# print(result[1])

bestschedule=schedule
besttime=result[1]

worstschedule=schedule
worsttime=result[1]

## Decreasing order of time
ls = [(time[i],i) for i in range(n)]
ls.sort(key=lambda x:x[0],reverse=True)
ls2=[]
for i in range(len(ls)):
	ls2.append(ls[i][1])
ls=ls2
result = find_schedule(graph,num_proc,ls)
schedule = result[0]
# sanity_check(schedule,num_tasks)
# print ("Decreasing order of time:")
# for proc in schedule:
	# print ([task for task in proc])
# assert finish_time(graph,schedule,time)==result[1]
# print (result[1])

if(result[1]<besttime):
	besttime=result[1]
	bestschedule=schedule

if(result[1]>worsttime):
	worsttime=result[1]
	worstschedule=schedule



## Random permutations
lim=40*n
ls = [i for i in range(n)]
shuffle(ls)
for i in range(lim):
	shuffle(ls)
	# print(ls)
	result = find_schedule(graph,num_proc,ls)
	schedule = result[0]
	# sanity_check(schedule,num_tasks)
	# for proc in schedule:
	# 	print [task for task in proc]
	# temp=finish_time(graph,schedule,time)
	# print(temp)
	# assert temp==result[1]
	# print temp,result[1]
	if(result[1]<besttime):
		besttime=result[1]
		bestschedule=schedule

	if(result[1]>worsttime):
		worsttime=result[1]
		worstschedule=schedule

sanity_check(bestschedule,num_tasks,besttime)
sanity_check(worstschedule,num_tasks,worsttime)

# print("Result of random permutations:")
# for proc in bestschedule:
# 	print [task for task in proc]
cout.write(str(besttime)+",")

# fd=open("result.txt",'a')
# fd.write(str(besttime)+",")
# fd.close()

# for proc in worstschedule:
# 	print [task for task in proc]
# print "\tWorst="+str(worsttime)
cout.write(str(worsttime)+",")



## Topologically sorted permutations
roots=[]
for i in range(n):
	if(pred[i]==[]):
		roots.append(i)

bs=[]
bt=1000000000
wt=0
ws=[]
lim=4*n
numroots=len(roots)
# permute roots lim times
for num in range(lim):
	shuffle(roots)
	topo=[]
	tk=0
	taken=[0 for i in range(n)]
	for i in range(numroots):
		topo.append(roots[i])
		taken[roots[i]]=1
		tk+=1

	while(tk<n):
		poss=[]
		for i in range(n):
			if taken[i]==1:
				continue
			temp=0
			for j in pred[i]:
				if(taken[j]==1):
					temp+=1
			if(temp==len(pred[i])):
				poss.append(i)

		order=[]
		lenp=len(poss)
		for i in range(lenp):
			a=poss[i]
			mind=-1
			distances=[]
			for j in range(len(topo)):
				if(topo[j] in pred[a]):
					mind=max(mind,j)
					distances.append(len(topo)-j)
			distances.sort()
			order.append((distances,poss[i]))

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
	# if(result[1]>wt):
	# 	wt=result[1]
	# 	ws=schedule

	# sanity_check(schedule,num_tasks)
	# for proc in schedule:
	# 	print [task for task in proc]
	# assert finish_time(graph,schedule,time)==result[1]

sanity_check(bs,num_tasks,bt)
# print ("Result of Topological sorts:")
# for proc in bs:
# 	print ([task for task in proc])
cout.write(str(bt)+"\n")

# fd=open("result.txt",'a')
# fd.write(str(bt)+"\n")
# fd.close()

# for proc in ws:
# 	print [task for task in proc]
# print "\tWorst="+str(wt)
