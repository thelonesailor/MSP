#!/bin/bash
	# g++ -O3 -std=c++11 -o generate rgpos.cpp
	# g++ -O3 -o gen_dot gen_dot.cpp

infolder="Case100"

genetic=0
our=0
for n in 100;
do
for e in 160; # ((e=$n-1;e<=2*$n;e+=20));
do
for p in 7;
do
for l in 1000;
do
for x in {0..179};
do	
	# java Convert <./50/rand0$x.stg >./Case50/in$x.txt
	# echo "Generating n=$n e=$e p=$p l=$l";
	# ./generate $n $e $p $l > ./input_files/$n-$e-$p-$l.txt 2>> errors.txt
	# python Random.py >./input_files/$n-$e-$p-$l-random.txt
	# ./gen_dot $p >./input_files/$n-$e-$p-$l.txt
	# echo "Generated";	

	# time python3 ga_msp.py <./input_files/$n-$e-$p-$l.txt
	# time python3 ga_msp.py <./input_files/$n-$e-$p-$l-random.txt
	echo "Genetic------------------------------";
	start=$SECONDS
    time python3 ga_msp.py <./$infolder/in$x.txt
	duration=$(( SECONDS - start ))
	genetic=$((duration + genetic))
	# time python3 ga_msp.py <./input_files/p1.txt
	
	# time python Machine.py <./input_files/$n-$e-$p-$l-random.txt
	# time python Machine.py <./Case50/in$x.txt	
	# echo "Genetic done------------------------------";

	# time python ListShd_p.py <./input_files/$n-$e-$p-$l.txt
	start=$SECONDS
	time python ListShd_p.py <./$infolder/in$x.txt
	duration=$(( SECONDS - start ))
	our=$((duration + our))
	
	# time python ListShd_p.py <./input_files/p1.txt	
	# echo "List scheduling done------------------------------";

	#rm $n-$e-$p-$l.txt
	# echo "------------------------------";
	echo $genetic;
	echo $our;
	
done;
done;
done;
done;
done;
	rm generate gen_dot
