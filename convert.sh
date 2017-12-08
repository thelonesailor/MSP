#!/bin/bash

infolder="300"
outfolder="Case300"

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