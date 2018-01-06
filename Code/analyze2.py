import csv
import sys

csvfile1=open(sys.argv[1], 'r')
reader1 = list(csv.reader(csvfile1, delimiter=','))

csvfile2=open(sys.argv[2], 'r')
reader2 = list(csv.reader(csvfile2, delimiter=','))

csvfile3=open(sys.argv[3], 'r')
reader3 = list(csv.reader(csvfile3, delimiter=','))

csvfile4=open(sys.argv[4], 'r')
reader4 = list(csv.reader(csvfile4, delimiter=','))



prakhargenetic = 0.0
ronakgenetic = 0.0
bestrandomls = 0.0
worstrandomls = 0.0
topologicalls = 0.0
swapsearch = 0.0

num = 15  # there are 180 task graphs

pg = []
rg = []
brls = []
wrls = []
tls = []
ss = []

for i in range(num):
	opt=int(reader2[i][0])

	t=((int(reader1[i][0])-opt)*100)/opt
	prakhargenetic+=t
	t=round(t,2)
	pg.append(t)

	t=((int(reader2[i][0])-opt)*100)/opt
	ronakgenetic+=t
	t=round(t,2)
	rg.append(t)

	t=((int(reader3[i][0])-opt)*100)/opt
	bestrandomls+=t
	t=round(t,2)
	brls.append(t)

	t=((int(reader3[i][1])-opt)*100)/opt
	worstrandomls+=t
	t=round(t,2)
	wrls.append(t)

	t=((int(reader3[i][2])-opt)*100)/opt
	topologicalls+=t
	t=round(t,2)
	tls.append(t)

	t=((int(reader4[i][0])-opt)*100)/opt
	swapsearch+=t
	t=round(t,2)
	ss.append(t)

prakhargenetic/=num
ronakgenetic/=num
bestrandomls/=num
worstrandomls/=num
topologicalls/=num
swapsearch/=num

prakhargenetic=round(prakhargenetic,2)
ronakgenetic=round(ronakgenetic,2)
bestrandomls=round(bestrandomls,2)
worstrandomls=round(worstrandomls,2)
topologicalls=round(topologicalls,2)
swapsearch=round(swapsearch,2)

pg.sort()
rg.sort()
brls.sort()
wrls.sort()
tls.sort()
ss.sort()

showavg=1
showmin=0
showmax=0
sp="     "

if showavg:
	sys.stdout.write("prakhargenetic=   "+str(prakhargenetic)+"%")
if showmin:
	sys.stdout.write(sp+str(pg[0])+"%")
if showmax:
	sys.stdout.write(sp+str(pg[num-1])+"%")
print()

if showavg:
	sys.stdout.write("ronakgenetic=     "+str(ronakgenetic)+"%")
if showmin:
	sys.stdout.write(sp+str(rg[0])+"%")
if showmax:
	sys.stdout.write(sp+str(rg[num-1])+"%")
print()

if showavg:
	sys.stdout.write("bestrandomls=     "+str(bestrandomls)+"%")
if showmin:
	sys.stdout.write(sp+str(brls[0])+"%")
if showmax:
	sys.stdout.write(sp+str(brls[num-1])+"%")
print()

if showavg:
	sys.stdout.write("worstrandomls=    "+str(worstrandomls)+"%")
if showmin:
	sys.stdout.write(sp+str(wrls[0])+"%")
if showmax:
	sys.stdout.write(sp+str(wrls[num-1])+"%")
print()

if showavg:
	sys.stdout.write("topologicalls=    "+str(topologicalls)+"%")
if showmin:
	sys.stdout.write(sp+str(tls[0])+"%")
if showmax:
	sys.stdout.write(sp+str(tls[num-1])+"%")
print()

if showavg:
	sys.stdout.write("swapsearch=       "+str(swapsearch)+"%")
if showmin:
	sys.stdout.write(sp+str(ss[0])+"%")
if showmax:
	sys.stdout.write(sp+str(ss[num-1])+"%")
print()
