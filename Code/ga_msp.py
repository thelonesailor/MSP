from random import randint,shuffle
import sys
from sys import stdin, stdout
from heapq import heappush,heappop

N = 500  # population size, assumed even
maxiterations = 100
prob_crossover = 1.0
prob_mutation = 0.05
cmax = 0
maxheight=0
beststring=[]
n,m,p = map(int,stdin.readline().split())
h=[-1 for i in range(n)]
h_=[-1 for i in range(n)]

time=list(map(int,stdin.readline().split()))

succ=[[] for i in range(n)]
pred=[[] for i in range(n)]
graph=[[0 for j in range(n)] for i in range(n)]
# print("arrays declared")

#tasks,edges,processors
def main():

	for i in range(m):
		u,v = map(int,stdin.readline().split())
		# u->v
		graph[u][v]=1

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

	for i in range(n):
		height(i)
		if(h[i]==-1):
			print("Something Wrong for h["+str(i)+"]  2")

	# print(n)
	# print(m)
	# print(sum(time))
	# print((time))
	# print(h)
	initialise_h_()
	# print(h_)

	find_schedule()


def find_schedule():

	pop=[]
	for i in range(N):
		#print("generating "+str(i))
		temp=generate_schedule()
		# print(temp)
		pop.append(temp)


	global maxiterations,cmax
	global prob_crossover,beststring
	fmin=0
	bs=1000000000
	bbs=[]
	for i in range(0,maxiterations):

		ft=[]
		# assert N==len(pop)
		fmin=1000000000
		for j in range(0,len(pop)):
			# print(j)
			# print(str(i)+"  pop["+str(j)+"]="+str(pop[j]))
			pop[j]=list(pop[j])
			ft.append(compute_FT(pop[j]))
			cmax=max(cmax,ft[j])
			fmin=min(fmin,ft[j])
		bs=min(bs,fmin)
		# print(fmin)
		nsum=0
		fitness=[]
		minj=-1
		minf=1000000000
		for j in range(0,N):
			fitness.append(cmax-ft[j])
			nsum+=fitness[j]
			if(fitness[j]<minf):
				minf=fitness[j]
				minj=j

		# assert minj>-1

		if(len(bbs)>0):
			pop[minj]=list(bbs)

		npop=len(pop)
		# assert N==npop

		newpop,beststring=Reproduction(pop,fitness,nsum)

		tmp=[]
		for j in range(0,npop,2):
			s1=j
			s2=j+1

			ns1,ns2=crossover(newpop[s1],newpop[s2],prob_crossover)

			tmp.append(ns1)
			tmp.append(ns2)

		pop=[]
		for s in tmp:
			news=mutation(s,prob_mutation)
			pop.append(list(news))
		if(bbs==[] or compute_FT(beststring)<compute_FT(bbs)):
			bbs=beststring
		check(beststring)

	temp=compute_FT(bbs)
	# fd=open("result.txt",'a')
	# fd.write(str(temp)+",")
	# fd.close()

	sys.stdout.write(str(temp)+"\n")
	# print(temp)
	# for a in bbs:
	# 	print(a)


def check(S):
	a=[0 for i in range(n)]
	for i in range(p):
		l=len(S[i])

		for j in range(l):
			a[S[i][j]]+=1


		for j in range(1,l):
			if(h_[S[i][j]]<h_[S[i][j-1]]):
				print("Wr")

	for i in range(n):
		if(a[i]<1):
			print(i)
			print(S)

			print("Missing element")
		elif(a[i]>1):
			print("Multiple element")

def mutation(A,prob):

	newA=list(A)
	r=randint(0,1000)
	if(float(r)/1000>prob):
		return newA

	r=randint(0,n-1)
	ri=0
	rj=0
	for i in range(p):
		l=len(newA[i])
		for j in range(l):
			if(newA[i][j]==r):
				ri=i
				rj=j
				break

	f=0
	for i in range(p):
		l=len(newA[i])
		for j in range(l):
			if(h_[newA[i][j]]==h_[r] and newA[i][j]!=r):
				f=1
				# swap(A[i][j],A[ri][rj])
				t=newA[i][j]
				newA[i][j]=newA[ri][rj]
				newA[ri][rj]=t
				break
		if(f==1):
			break

	return newA

def crossover(A,B,prob):
	check(A)
	check(B)

	global maxheight,p,h_
	c=randint(0,maxheight)

	if(float(c)/maxheight>prob):#do only with probability prob
		return A,B

	newA=[[] for i in range(p)]
	newB=[[] for i in range(p)]
	for i in range(p):
		Aj=len(A[i])
		for j in range(len(A[i])):
			if(h_[A[i][j]]>c):
				Aj=j
				break

		Bj=len(B[i])
		for j in range(len(B[i])):
			if(h_[B[i][j]]>c):
				Bj=j
				break

		# start-Aj-1 Aj to end
		# start-Bj-1 Bj to end
		if(Bj==len(B[i])):
			newA[i]=A[i][:Aj]
		else:
			newA[i]=A[i][:Aj]+B[i][Bj:]

		if(Aj==len(A[i])):
			newB[i]=B[i][:Bj]
		else:
			newB[i]=B[i][:Bj]+A[i][Aj:]

	# print(c)
	# print(A)
	# print(B)
	# print(newA)
	# print(newB)
	return newA,newB



def Reproduction(pop,fitness,nsum):
	newpop=[]
	npop=len(pop)
	assert (npop==N)
	for i in range(1,npop):
		r=randint(1,nsum)
		temp=0
		for j in range(N):
			temp+=fitness[j]
			if(r<=temp):
				newpop.append(pop[j])
				break

	maxj=-1
	f=0
	for j in range(N):
		if(fitness[j]>f):
			f=fitness[j]
			maxj=j

	newpop.append(pop[maxj])
	return newpop,pop[maxj]

def compute_FT(S):
	start=[-1 for i in range(n)]
	finish=[-1 for i in range(n)]

	# check
	pos = [(-1,-1) for i in range(n)]
	for i in range(len(S)) :
		for j in range(len(S[i])) :
			#print "Schedule:",schedule[i][j]
			pos[S[i][j]]=(i,j)
	for elem in pos :
		if elem==(-1,-1):
			print ("Repeat Error")


	done=[0 for i in range(n)]
	stack=[]

	for ls in S:
		l=len(ls)
		for j in range(l):
			stack.append(ls[j])

	prv=[-1 for i in range(n)]
	for i in range(p):
		l=len(S[i])
		for j in range(1,l):
			prv[S[i][j]]=S[i][j-1]



	while(len(stack)>0):
		a=stack[-1]
		if(done[a]==0):

			if(prv[a]==-1 and len(pred[a])==0):
				start[a]=0
				finish[a]=start[a]+time[a]
				done[a]=1
				stack.pop()
				continue

			f=0
			for b in pred[a]:
				if(done[b]==0):
					stack.append(b)
					f+=1
			if(prv[a]>-1 and prv[a] not in pred[a] and done[prv[a]]==0):
				stack.append(prv[a])
				f+=1
			if(f==0):
				for pr in pred[a]:
					start[a]=max(start[a],finish[pr])
				if(prv[a]>-1 and prv[a] not in pred[a]):
					start[a]=max(start[a],finish[prv[a]])
				finish[a]=start[a]+time[a]
				done[a]=1
				stack.pop()
		else:
			stack.pop()
		#print(len(stack))

	return max(finish)

def initialise_h_():
	global maxheight,h_

	maxheight=0
	for i in range(n):

		maxh=-1
		for t in pred[i]:
			if(h[t]>maxh):
				maxh=h[t]

		minh=1000000000
		for t in succ[i]:
			if(h[t]<minh):
				minh=h[t]

		if(maxh==-1 or minh==1000000000):
			h_[i]=h[i]
		else:
			# print("i="+str(i)+" "+str(maxh+1)+" "+str(minh-1))
			h_[i]=randint(maxh+1,minh-1)

		maxheight=max(maxheight,h_[i])

def generate_schedule():

	global h_,p,maxheight


	G=[set() for i in range(maxheight+1)]
	for i in range(0,n):
		G[h_[i]].add(i)

	S=[[] for i in range(p)]
	np=[i for i in range(p)]
	shuffle(np)
	for i in range(p-1):#for first p-1 processors
		for he in range(0,maxheight+1):
			if(len(G[he])>0):
				r=randint(0,len(G[he]))
				j=0
				gtemp=set(G[he])
				for t in G[he]:
					gtemp.remove(t)
					S[np[i]].append(t)

					j+=1
					if(j>=r):
						break
				G[he]=set(gtemp)

	#for last processor
	for he in range(0,maxheight+1):
		if(len(G[he])>0):
			gtemp=set(G[he])
			for t in G[he]:
				gtemp.remove(t)
				S[np[-1]].append(t)
			G[he]=gtemp
			assert G[he]==set()

	return S





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


if __name__ == "__main__":
	main()
