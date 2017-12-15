#!/bin/bash

our=0

for infolder in {"Case50_2","Case50_4","Case50_8","Case50_16","Case100_2","Case100_4","Case100_8","Case100_16"}	
do
	fname=./Results/randtop/"$infolder"_rtop.csv

	infolder=Inputs/$infolder

	rm $fname
	touch $fname

for x in {0..179};
do	

	echo "Random & Topologically sorted----------------------------";
	start=$SECONDS
	time python3 ListShd_p.py <./$infolder/in$x.txt >> $fname
	duration=$(( SECONDS - start ))
	our=$((duration + our))


	echo "------------------------------";
	echo $our;
	
	echo "$infolder/in$x.txt";
	
done;
done;
