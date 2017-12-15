#!/bin/bash

geneticr=0

for infolder in {"Case50_2","Case50_4","Case50_8","Case50_16","Case100_2","Case100_4","Case100_8","Case100_16"}	
do
	fname=./Results/genetic2/"$infolder"_gr.csv

	infolder=Inputs/$infolder

	rm $fname
	touch $fname

for x in {0..179};
do	

	echo "Genetic2-Ronak-------------------------";
	start=$SECONDS
	time python Machine.py <./$infolder/in$x.txt >> $fname   
	duration=$(( SECONDS - start ))
	geneticr=$((duration + geneticr))


	echo "------------------------------";
	echo $geneticr;
	
	echo "$infolder/in$x.txt";
	
done;
done;
