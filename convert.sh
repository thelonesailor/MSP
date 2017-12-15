#!/bin/bash

javac Convert.java

for infolder in {50,100};
do 
for p in {2,4,8,16};
do 

outfolder=Inputs/"Case$infolder"_$p
echo $outfolder;


for x in {0..9};
do	
	java Convert $p <./$infolder/rand000$x.stg >./$outfolder/in$x.txt
	echo $x
done;	
for x in {10..99};
do	
	java Convert $p <./$infolder/rand00$x.stg >./$outfolder/in$x.txt
	echo $x
done;	
for x in {100..179};
do	
	java Convert $p <./$infolder/rand0$x.stg >./$outfolder/in$x.txt
	echo $x
done;
done;
done;
	rm Convert.class mylist.class