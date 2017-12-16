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
bestrandomls=0.0
worstrandomls=0.0
topologicalls=0.0
swapsearch=0.0

num=180# there are 180 task graphs

pg=[]
rg=[]
brls=[]
wrls=[]
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
	bestrandomls+=t
	brls.append(t)

	t=((int(reader4[i][1])-opt)*100)/opt
	worstrandomls+=t
	wrls.append(t)

	t=((int(reader4[i][2])-opt)*100)/opt
	topologicalls+=t
	tls.append(t)

	t=((int(reader5[i][0])-opt)*100)/opt
	swapsearch+=t
	ss.append(t)

prakhargenetic/=num
ronakgenetic/=num
bestrandomls/=num
worstrandomls/=num
topologicalls/=num
swapsearch/=num

pg.sort()
rg.sort()
brls.sort()
wrls.sort()
tls.sort()
ss.sort()

sys.stdout.write("prakhargenetic=   "+str(prakhargenetic)+"%")
# sys.stdout.write("\t"+str(pg[num-1])+"%")
print()
sys.stdout.write("ronakgenetic=     "+str(ronakgenetic)+"%")
# sys.stdout.write("\t"+str(rg[num-1])+"%")
print()
sys.stdout.write("bestrandomls=     "+str(bestrandomls)+"%")
# sys.stdout.write("\t"+str(brls[num-1])+"%")
print()
sys.stdout.write("worstrandomls=    "+str(worstrandomls)+"%")
# sys.stdout.write("\t"+str(wrls[num-1])+"%")
print()
sys.stdout.write("topologicalls=    "+str(topologicalls)+"%")
# sys.stdout.write("\t"+str(tls[num-1])+"%")
print()
sys.stdout.write("swapsearch=       "+str(swapsearch)+"%")
# sys.stdout.write("\t"+str(ss[num-1])+"%")
print()
