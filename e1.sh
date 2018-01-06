#!/bin/bash
set -e

geneticp=0
echo "Running for 0..$2";

for infolder in {"Case50_2","Case50_4","Case50_8","Case50_16","Case100_2","Case100_4","Case100_8","Case100_16"}
do
	if [ $1 -eq 91527 ]
	then
		fname=./Result_files/genetic1/"$infolder"_gp.csv
	else
		fname=./Result_test/genetic1/"$infolder"_gp.csv
	fi

	infolder=Inputs/$infolder

	rm -f $fname
	touch $fname

for (( x=0; x <= $2; x++ ))
do

	echo "Genetic1-Prakhar-----------------------";
	start=$SECONDS
	time python3 Code/ga_msp.py <./$infolder/in$x.txt >> $fname
 	duration=$(( SECONDS - start ))
	geneticp=$((duration + geneticp))


	echo "------------------------------";
	echo $geneticp;

	echo "$infolder/in$x.txt";

done;
done;
