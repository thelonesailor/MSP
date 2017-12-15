#!/bin/bash

ffile=RESULT.txt
rm $ffile
touch $ffile
	
for infolder in {"Case50_2","Case50_4","Case50_8","Case50_16","Case100_2","Case100_4","Case100_8","Case100_16"}	
do
	echo "$infolder" >>$ffile;
	f1name=./Optimal/"$infolder"_OPT.csv
	f2name=./Results/genetic1/"$infolder"_gp.csv
	f3name=./Results/genetic2/"$infolder"_gr.csv
	f4name=./Results/randtop/"$infolder"_rtop.csv
	f5name=./Results/swapsearch/"$infolder"_ss.csv
		
	python3 analyze.py $f1name $f2name $f3name $f4name $f5name >>$ffile

	
	echo "-----------------------------------------------" >> $ffile;

done;
