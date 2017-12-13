#!/bin/bash

ffile=RESULT.txt
rm $ffile
touch $ffile
	
for infolder in {"Case50_2","Case50_4","Case50_8","Case50_16","Case100_2","Case100_4","Case100_8","Case100_16"}	
do
	echo "$infolder" >>$ffile;
	f1name=./Optimal/"$infolder"_OPT.csv
	f2name=./Results/"$infolder"_result.csv
	f3name=./Results/"$infolder"_rcus.csv
		
	python3 analyze1.py $f1name $f2name >>$ffile
	python3 analyze2.py $f1name $f3name >>$ffile
	
	echo "-----------------------------------------------" >> $ffile;

done;
