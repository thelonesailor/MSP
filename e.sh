#!/bin/bash
set -e

# echo "Running for 0..$2";

for infolder in {"Rand100","Rgpos100"};
do
for (( p=2; p <= $3; p++ ))
do
    if [ $1 -eq 91527 ]
	then
		fname1=./Result_files/genetic1/"$infolder$p"_gp.csv
        fname2=./Result_files/genetic2/"$infolder$p"_gr.csv
        fname3=./Result_files/randtop/"$infolder$p"_rtop.csv
        fname4=./Result_files/swapsearch/"$infolder$p"_ss.csv

	else
		fname1=./Result_test/genetic1/"$infolder$p"_gp.csv
        fname2=./Result_test/genetic2/"$infolder$p"_gr.csv
        fname3=./Result_test/randtop/"$infolde$p"_rtop.csv
        fname4=./Result_test/swapsearch/"$infolder$p"_ss.csv

	fi

    rm -f $fname1 $fname2 $fname3 $fname4
	touch $fname1 $fname2 $fname3 $fname4



for (( x=0; x <= $2; x++ ))
do

	echo "Genetic1-Prakhar-----------------------";
	time python3 Code/ga_msp.py <./Inputs/$infolder/in$x-$p.txt >> $fname1 &
    echo "Genetic2-Ronak-------------------------";
	time python Code/Machine.py <./Inputs/$infolder/in$x-$p.txt >> $fname2 &
    echo "Random & Topologically sorted----------------------------";
	time python3 Code/ListShd_p.py <./Inputs/$infolder/in$x-$p.txt >> $fname3 &
    echo "Swap search---------------------------";
    time python Code/ListShd.py <./Inputs/$infolder/in$x-$p.txt >>$fname4 &
	echo "------------------------------";

	echo "$infolder/in$x-$p.txt";
done;
done;
done;
wait
