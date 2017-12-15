#!/bin/bash

ss=0

for infolder in {"Case50_2","Case50_4","Case50_8","Case50_16","Case100_2","Case100_4","Case100_8","Case100_16"}	
do
	fname=./Results/swapsearch/"$infolder"_ss.csv

	infolder=Inputs/$infolder

	rm $fname
	touch $fname

for x in {0..179};
do	

	echo "Swap search---------------------------";
	start=$SECONDS
	time python ListShd.py <./$infolder/in$x.txt >>$fname
	duration=$(( SECONDS - start ))
	ss=$((duration + ss))
	

	echo "------------------------------";
	echo $ss;
	
	echo "$infolder/in$x.txt";
	
done;
done;
