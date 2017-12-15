#!/bin/bash

geneticp=0

for infolder in {"Case50_2","Case50_4","Case50_8","Case50_16","Case100_2","Case100_4","Case100_8","Case100_16"}	
do
	fname=./Results/genetic1/"$infolder"_gp.csv

	infolder=Inputs/$infolder

	rm $fname
	touch $fname

for x in {0..179};
do	

	echo "Genetic1-Prakhar-----------------------";
	start=$SECONDS
	time python3 ga_msp.py <./$infolder/in$x.txt >> $fname
 	duration=$(( SECONDS - start ))
	geneticp=$((duration + geneticp))

	
	echo "------------------------------";
	echo $geneticp;
	
	echo "$infolder/in$x.txt";
	
done;
done;
