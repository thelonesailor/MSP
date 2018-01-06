#!/bin/bash

s="$(date +"%m%d%y%T")"
	g++ -O3 -std=c++11 -o generate$s Generators/rgpos.cpp

for n in {100..100};
do
for p in {2..10};
do
for e in {150..150};
do
for l in {1000..1000};
do
for i in {0..14};
do
    echo "Generating $n $p"
	time python Generators/Random.py $n $p >./Inputs/Rand$n/in$i-$p.txt
	time ./generate$s $n $e $p $l > ./Inputs/Rgpos$n/in$i-$p.txt

done;
done;
done;
done;
done;

	rm generate$s
