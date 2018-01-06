#!/bin/bash

ffile=Result_files/RESULT.txt
rm $ffile
touch $ffile

for infolder in {"Case50_2","Case50_4","Case50_8","Case50_16","Case100_2","Case100_4","Case100_8","Case100_16"}
do
	echo "$infolder" >>$ffile;
	f1name=./Optimal_values/"$infolder"_OPT.csv
	f2name=./Result_files/genetic1/"$infolder"_gp.csv
	f3name=./Result_files/genetic2/"$infolder"_gr.csv
	f4name=./Result_files/randtop/"$infolder"_rtop.csv
	f5name=./Result_files/swapsearch/"$infolder"_ss.csv

	python3 Code/analyze.py $f1name $f2name $f3name $f4name $f5name >>$ffile


	echo "-----------------------------------------------" >> $ffile;

done;

for inf in {"Rand100","Rgpos100"}
do
for p in {2..10}
do
	infolder="$inf$p"
	echo "$inf"_"$p" >>$ffile;
	f2name=./Result_files/genetic1/"$infolder"_gp.csv
	f3name=./Result_files/genetic2/"$infolder"_gr.csv
	f4name=./Result_files/randtop/"$infolder"_rtop.csv
	f5name=./Result_files/swapsearch/"$infolder"_ss.csv

	python3 Code/analyze2.py $f2name $f3name $f4name $f5name >>$ffile


	echo "-----------------------------------------------" >> $ffile;

done;
done;
