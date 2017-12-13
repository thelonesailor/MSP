import csv
import sys

csvfile=open(sys.argv[1], 'r')
reader = list(csv.reader(csvfile, delimiter=','))


csvfile2=open(sys.argv[2], 'r')
reader2 = list(csv.reader(csvfile2, delimiter=','))

prakhargenetic=0.0
ronakgenetic=0.0
randomls=0.0
topologicalls=0.0

num=180

# print(len(reader))
# print(len(reader2))
pg=[]
rg=[]
rls=[]
tls=[]
for i in range(num):
	opt=int(reader[i][2])

	t=(int(reader2[i][0])-opt)*100/opt
	prakhargenetic+=t
	pg.append(t)
	
	t=(int(reader2[i][1])-opt)*100/opt
	ronakgenetic+=t
	rg.append(t)
	# print(i)

	t=(int(reader2[i][2])-opt)*100/opt
	randomls+=t
	rls.append(t)

	t=(int(reader2[i][3])-opt)*100/opt
	topologicalls+=t
	tls.append(t)


prakhargenetic/=num
ronakgenetic/=num
randomls/=num
topologicalls/=num

pg.sort()
rg.sort()
rls.sort()
tls.sort()

sys.stdout.write("prakhargenetic= "+str(prakhargenetic)+"%")
# sys.stdout.write("\t"+str(pg[num-1])+"%")
print()
sys.stdout.write("ronakgenetic=   "+str(ronakgenetic)+"%")
# sys.stdout.write("\t"+str(rg[num-1])+"%")
print()
sys.stdout.write("randomls=       "+str(randomls)+"%")
# sys.stdout.write("\t"+str(rls[num-1])+"%")
print()
sys.stdout.write("topologicalls=  "+str(topologicalls)+"%")
# sys.stdout.write("\t"+str(tls[num-1])+"%")
print()
