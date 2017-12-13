#!/bin/bash

geneticp=0
geneticr=0
our=0
ss=0

for infolder in {"Case50_2","Case50_4","Case50_8","Case50_16","Case100_2","Case100_4","Case100_8","Case100_16"}	
do
	fname=./Results/1"$infolder"_temp.csv

	infolder=Inputs/$infolder

	echo $fname
	rm $fname
	touch $fname

for x in {0..0};
do	


	echo "Genetic1-Prakhar-----------------------";
	start=$SECONDS
	time python3 ga_msp.py <./$infolder/in$x.txt >> $fname
 	duration=$(( SECONDS - start ))
	geneticp=$((duration + geneticp))

	
	echo "Genetic2-Ronak-------------------------";
	start=$SECONDS
	time python Machine.py <./$infolder/in$x.txt >> $fname   
	duration=$(( SECONDS - start ))
	geneticr=$((duration + geneticr))

	
	echo "Random & Topologically sorted----------------------------";
	start=$SECONDS
	time python3 ListShd_p.py <./$infolder/in$x.txt >> $fname
	duration=$(( SECONDS - start ))
	our=$((duration + our))


	echo "Swap search---------------------------";
	start=$SECONDS
	time python ListShd.py <./$infolder/in$x.txt >>$fname
	duration=$(( SECONDS - start ))
	ss=$((duration + ss))
	

	echo "------------------------------";
	echo $geneticp;
	echo $geneticr;
	echo $our;
	echo $ss;
	
	echo "$infolder/in$x.txt";
	
done;
done;
