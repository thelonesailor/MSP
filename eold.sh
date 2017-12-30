#!/bin/bash
s="$(date +"%m%d%y%T")"$1
	g++ -O3 -std=c++11 -o generate$s Generators/rgpos.cpp
	g++ -O3 -std=c++11 -o gen_dot$s Generators/gen_dot.cpp

# rand=0 for Generators/rgpos.cpp
# rand=1 for Generators/gen_dot.cpp
# rand=2 for Generators/Random.py
rand=$1

for n in {100..100};
do
for e in 240; # ((e=$n-1;e<=2*$n;e+=20));
do
for p in 4;
do
for l in 1000;
do

	echo "Generating n=$n e=$e p=$p l=$l , rand=$rand";
	if [ $rand -eq 0 ]
	then
		time ./generate$s $n $e $p $l > ./Inputs/$n-$e-$p-$l-$rand.txt
	elif [ $rand -eq 1 ]
	then
		time ./gen_dot$s $p >./Inputs/$n-$e-$p-$l-$rand.txt
	elif [ $rand -eq 2]
	then
		time python Generators/Random.py $n $p >./Inputs/$n-$e-$p-$l-$rand.txt
	else
		echo "Invalid parameter given";
	fi
	echo "Generated";

	echo "Genetic1-Prakhar-----------------------";
	time python3 Code/ga_msp.py <./Inputs/$n-$e-$p-$l-$rand.txt

	echo "Genetic2-Ronak-------------------------";
	time python Code/Machine.py <./Inputs/$n-$e-$p-$l-$rand.txt

	echo "Random & Topologically sorted----------------------------";
	time python3 Code/ListShd_p.py <./Inputs/$n-$e-$p-$l-$rand.txt

	echo "Swap search---------------------------";
	time python Code/ListShd.py <./Inputs/$n-$e-$p-$l-$rand.txt

	rm ./Inputs/$n-$e-$p-$l-$rand.txt

done;
done;
done;
done;
	rm generate$s gen_dot$s
