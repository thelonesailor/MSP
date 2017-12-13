#!/bin/bash

for infolder in {50,100};
do 
for p in {2,4,8,16};
do 

outfolder=Inputs/"Case$infolder"_$p
echo $outfolder;

javac Convert.java

for x in {0..9};
do	
	java Convert <./$infolder/rand000$x.stg >./$outfolder/in$x.txt
	echo $x
done;	
for x in {10..99};
do	
	java Convert <./$infolder/rand00$x.stg >./$outfolder/in$x.txt
	echo $x
done;	
for x in {100..179};
do	
	java Convert <./$infolder/rand0$x.stg >./$outfolder/in$x.txt
	echo $x
done;
done;
done;
	rm Convert.class mylist.class