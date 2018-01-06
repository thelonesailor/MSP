#!/bin/bash
set -e

our=0
echo "Running for 0..$2";

for infolder in {"Case50_2","Case50_4","Case50_8","Case50_16","Case100_2","Case100_4","Case100_8","Case100_16"}
do
	if [ $1 -eq 91527 ]
	then
		fname=./Result_files/randtop/"$infolder"_rtop.csv
	else
		fname=./Result_test/randtop/"$infolder"_rtop.csv
	fi

	infolder=Inputs/$infolder

	rm -f $fname
	touch $fname

for (( x=0; x <= $2; x++ ))
do

	echo "Random & Topologically sorted----------------------------";
	start=$SECONDS
	time python3 Code/ListShd_p.py <./$infolder/in$x.txt >> $fname
	duration=$(( SECONDS - start ))
	our=$((duration + our))


	echo "------------------------------";
	echo $our;

	echo "$infolder/in$x.txt";

done;
done;
