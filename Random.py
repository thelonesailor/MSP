import sys,random
from math import sqrt
cin = sys.stdin

from datetime import datetime
random.seed(datetime.now())

def printf(format,*args):
	sys.stdout.write(format % args)
def rint(lim,mode):
	if mode==1:
		seed = random.randint(0,lim*lim)
		return int(sqrt(seed))
	elif mode==2:
		return random.randint(0,lim)
	else:
		print "Mode Error"
		return 0
n = int(cin.readline())
max_edge = (n*(n-1))/2
# print max_edge
nedge = rint(max_edge,2)
# print nedge
nproc = random.randint(5,10)
adj = [[0]*n for i in xrange(n)]
ct=0
while ct<nedge:
	a,b = random.randint(0,n-1),random.randint(0,n-1)
	if a==b:
		continue
	if a>b:
		a,b = b,a
	# a<=b
	adj[a][b]=1
	ct+=1
reach = [[elem for elem in ls] for ls in adj]
for i in xrange(n):
	reach[i][i]=1
for k in xrange(n):
	for i in xrange(n):
		for j in xrange(n):
			if reach[i][k] and reach[k][j] :
				reach[i][j]=1
for i in xrange(n):
	reach[i][i]=0

reach2 = [[0 for i in xrange(n)] for j in xrange(n)]
for i in xrange(n):
	for j in xrange(n):
		reach2[i][j]=reach[i][j]

for i in xrange(n):
	for j in xrange(n):
		if reach[i][j] :
			for k in xrange(n):
				if reach[j][k] and reach[i][k]:
					reach2[i][k]=0
reach=reach2

time = [random.randint(1,50) for i in xrange(n)]
nedg=0
for i in xrange(n):
	for j in xrange(n):
		nedg+=1 if reach[i][j] else 0 
printf("%d %d %d\n",n,nedg,nproc)
for i in xrange(len(time)):
	if i+1==len(time):
		printf("%d",time[i])
	else:	
		printf("%d ",time[i])
printf("\n")
for i in xrange(n):
	for j in xrange(n):
		if reach[i][j] :
			print i,j