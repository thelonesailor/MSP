from random import randint
from sys import stdin, stdout
#currently the same as other

N=500#population size, assumed even
maxiterations=100
prob_crossover=1.0
prob_mutation=0.05
cmax=0
maxheight=0
beststring=[]

#number of tasks,number of edges,number of processors
n,m,p = map(int,stdin.readline().split())
h=[-1 for i in range(0,n)]
h_=[-1 for i in range(0,n)]

time=list(map(int,stdin.readline().split()))

succ=[[] for i in range(0,n)]
pred=[[] for i in range(0,n)]
print("arrays declared")

#tasks,edges,processors
def main():
	for i in range(0,m):
		u,v = map(int,stdin.readline().split())
		# u->v
		succ[u].append(v)
		pred[v].append(u)


	for i in range(0,n):
		height(i)
		if(h[i]==-1):
			print("Something Wrong for h["+str(i)+"]  2")

	print(n)
	print(m)
	print(time)
	print(h)

	find_schedule()
	# print(compute_FT([[1, 2, 5, 7], [0, 3, 4, 6]]))

def find_schedule():

	initialise_h_()
	print(h_)

	pop=[]
	for i in range(0,N):
		print("generating "+str(i))
		temp=generate_schedule()
		# print(temp)
		pop.append(temp)


	global maxiterations,cmax
	global prob_crossover,beststring
	fmin=0
	for i in range(0,maxiterations):

		ft=[]
		assert N==len(pop)
		fmin=1000000000
		for j in range(0,len(pop)):
			# print(j)
			# print(str(i)+"  pop["+str(j)+"]="+str(pop[j]))
			pop[j]=list(pop[j])
			ft.append(compute_FT(pop[j]))
			cmax=max(cmax,ft[j])
			fmin=min(fmin,ft[j])

		print(fmin)
		nsum=0
		fitness=[]
		minj=0
		minf=1000000000
		for j in range(0,N):
			fitness.append(cmax-ft[j])
			nsum+=fitness[j]
			if(fitness[j]<minf):
				minf=fitness[j]
				minj=j

		if(beststring!=[]):
			pop[minj]=list(beststring)

		npop=len(pop)
		assert N==npop

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

	print(fmin)
	print("Best string ="+str(beststring))

def mutation(A,prob):

	newA=list(A)
	r=randint(0,1000)
	if(float(r)/1000>prob):
		return newA

	r=randint(0,n-1)
	ri=0
	rj=0
	for i in range(0,p):
		l=len(newA[i])
		for j in range(0,l):
			if(newA[i][j]==r):
				ri=i
				rj=j
				break

	f=0
	for i in range(0,p):
		l=len(newA[i])
		for j in range(0,l):
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
	global maxheight,p,h_
	c=randint(0,maxheight)

	if(float(c)/maxheight>prob):#do only with probability prob
		return A,B

	newA=[[] for i in range(0,p)]
	newB=[[] for i in range(0,p)]
	for i in range(0,p):
		Aj=len(A[i])
		for j in range(0,len(A[i])):
			if(h_[A[i][j]]>c):
				Aj=j
				break

		Bj=len(B[i])
		for j in range(0,len(B[i])):
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

	for i in range(1,npop):
		r=randint(1,nsum)
		temp=0
		for j in range(0,N):
			temp+=fitness[j]
			if(r<=temp):
				newpop.append(pop[j])
				break

	maxj=-1
	f=0
	for j in range(0,N):
		if(fitness[j]>f):
			f=fitness[j]
			maxj=j

	newpop.append(pop[maxj])
	return newpop,pop[maxj]

def compute_FT(S):
	start=[-1 for i in range(0,n)]
	finish=[-1 for i in range(0,n)]

	for i in range(0,p):
		l=len(S[i])
		temp=0
		for j in range(0,l):
			start[S[i][j]]=temp
			finish[S[i][j]]=start[S[i][j]]+time[S[i][j]]
			temp+=time[S[i][j]]

	for k in range(0,m+p):
		for i in range(0,p):
			l=len(S[i])

			for j in range(0,l):
				if(j>0):
					start[S[i][j]]=max(start[S[i][j]],start[S[i][j-1]])
				temp=0
				for a in pred[S[i][j]]:
					temp=max(temp,finish[a])

				start[S[i][j]]=max(start[S[i][j]],temp)
				finish[S[i][j]]=start[S[i][j]]+time[S[i][j]]

	fn=0
	for i in range(0,n):
		fn=max(fn,finish[i])


	# print(start)
	# print(finish)

	return fn

def initialise_h_():
	global maxheight,h_

	maxheight=0
	for i in range(0,n):

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
			print("i="+str(i)+" "+str(maxh+1)+" "+str(minh-1))
			h_[i]=randint(maxh+1,minh-1)

		maxheight=max(maxheight,h_[i])

def generate_schedule():

	global h_,p,maxheight


	G=[set() for i in range(0,maxheight+1)]
	for i in range(0,n):
		G[h_[i]].add(i)

	S=[[] for i in range(0,p)]
	for i in range(0,p-1):#for first p-1 processors
		for he in range(0,maxheight+1):
			if(len(G[he])>0):
				r=randint(0,len(G[he]))
				j=0
				gtemp=set(G[he])
				for t in G[he]:
					gtemp.remove(t)
					S[i].append(t)

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
				S[p-1].append(t)
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
