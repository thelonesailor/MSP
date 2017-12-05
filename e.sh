#!/bin/bash
	# g++ -O3 -std=c++11 -o generate rgpos.cpp
	# g++ -O3 -o gen_dot gen_dot.c
for n in 100;
do
for e in 120; # ((e=$n-1;e<=2*$n;e+=20));
do
for p in 7;
do
for l in 1000;
do
	echo "Generating n=$n e=$e p=$p l=$l";
	# ./generate $n $e $p $l > ./input_files/$n-$e-$p-$l.txt 2>> errors.txt
	python Random.py >./input_files/$n-$e-$p-$l-random.txt
	echo "Generated";	

	# time python3 ga_msp.py <./input_files/$n-$e-$p-$l.txt
	time python3 ga_msp.py <./input_files/$n-$e-$p-$l-random.txt
	# time python3 ga_msp.py <./input_files/p1.txt
	
	# time python Machine.py <./input_files/$n-$e-$p-$l-random.txt	
	echo "Genetic done------------------------------";

	# time python ListShd_p.py <./input_files/$n-$e-$p-$l.txt
	time python ListShd_p.py <./input_files/$n-$e-$p-$l-random.txt
	# time python ListShd_p.py <./input_files/p1.txt	
	# echo "List scheduling done------------------------------";

	#rm $n-$e-$p-$l.txt
	echo "------------------------------";
done;
done;
done;
done;
	# rm generate
