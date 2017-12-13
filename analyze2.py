import csv
import sys

csvfile=open(sys.argv[1], 'r')
reader = list(csv.reader(csvfile, delimiter=','))


csvfile2=open(sys.argv[2], 'r')
reader2 = list(csv.reader(csvfile2, delimiter=','))

swapsearch=0.0

num=180

ss=[]
for i in range(num):
	opt=int(reader[i][2])

	t=(int(reader2[i][0])-opt)*100/opt
	swapsearch+=t
	ss.append(t)
	


swapsearch/=num

ss.sort()

sys.stdout.write("swapsearch=     "+str(swapsearch)+"%")
# sys.stdout.write("\t"+str(ss[num-1])+"%")
print()

