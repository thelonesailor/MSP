import csv
import sys

csvfile=open(sys.argv[1], 'r')
reader = list(csv.reader(csvfile, delimiter=','))


csvfile2=open(sys.argv[2], 'r')
reader2 = list(csv.reader(csvfile2, delimiter=','))

csvfile3=open(sys.argv[3], 'r')
reader3 = list(csv.reader(csvfile3, delimiter=','))

csvfile4=open(sys.argv[4], 'r')
reader4 = list(csv.reader(csvfile4, delimiter=','))

csvfile5=open(sys.argv[5], 'r')
reader5 = list(csv.reader(csvfile5, delimiter=','))


prakhargenetic=0.0
ronakgenetic=0.0
randomls=0.0
worstls=0.0
topologicalls=0.0
swapsearch=0.0

num=180

# print(len(reader))
# print(len(reader2))
pg=[]
rg=[]
rls=[]
wls=[]
tls=[]
ss=[]

for i in range(num):
	opt=int(reader[i][2])

	t=((int(reader2[i][0])-opt)*100)/opt
	prakhargenetic+=t
	pg.append(t)
	
	t=((int(reader3[i][0])-opt)*100)/opt
	ronakgenetic+=t
	rg.append(t)

	t=((int(reader4[i][0])-opt)*100)/opt
	randomls+=t
	rls.append(t)

	t=((int(reader4[i][1])-opt)*100)/opt
	worstls+=t
	wls.append(t)

	t=((int(reader4[i][2])-opt)*100)/opt
	topologicalls+=t
	tls.append(t)

	t=((int(reader5[i][0])-opt)*100)/opt
	swapsearch+=t
	ss.append(t)

prakhargenetic/=num
ronakgenetic/=num
randomls/=num
worstls/=num
topologicalls/=num
swapsearch/=num

pg.sort()
rg.sort()
rls.sort()
wls.sort()
tls.sort()
ss.sort()

sys.stdout.write("prakhargenetic= "+str(prakhargenetic)+"%")
# sys.stdout.write("\t"+str(pg[num-1])+"%")
print()
sys.stdout.write("ronakgenetic=   "+str(ronakgenetic)+"%")
# sys.stdout.write("\t"+str(rg[num-1])+"%")
print()
sys.stdout.write("randomls=       "+str(randomls)+"%")
# sys.stdout.write("\t"+str(rls[num-1])+"%")
print()
sys.stdout.write("worstls=        "+str(worstls)+"%")
# sys.stdout.write("\t"+str(wls[num-1])+"%")
print()
sys.stdout.write("topologicalls=  "+str(topologicalls)+"%")
# sys.stdout.write("\t"+str(tls[num-1])+"%")
print()
sys.stdout.write("swapsearch=     "+str(swapsearch)+"%")
# sys.stdout.write("\t"+str(ss[num-1])+"%")
print()
