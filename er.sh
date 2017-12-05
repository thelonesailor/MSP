#!/bin/bash
	g++ -O3 -std=c++11 -o generate rgpos.cpp
for n in 40;
do
for e in 39; # ((e=$n-1;e<=2*$n;e+=20));
do
for p in 5;
do
for l in 100;
do
	echo "Generating n=$n e=$e p=$p l=$l";
	#./generate $n $e $p $l >./input_files/ $n-$e-$p-$l.txt 2>> errors.txt
	echo "Generated";	
	# time python Machine.py <./input_files/$n-$e-$p-$l.txt
	time python ListShd.py <./input_files/$n-$e-$p-$l.txt

	
	#rm $n-$e-$p-$l.txt
	echo "------------------------------";
done;
done;
done;
done;
	rm generate
