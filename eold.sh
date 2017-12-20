#!/bin/bash
	g++ -O3 -std=c++11 -o generate Generators/rgpos.cpp
	g++ -O3 -std=c++11 -o gen_dot Generators/gen_dot.cpp

# rand=0 for Generators/rgpos.cpp
# rand=1 for Generators/Random.py
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
		time ./generate $n $e $p $l > ./Inputs/$n-$e-$p-$l.txt
		# time ./gen_dot $p >./Inputs/$n-$e-$p-$l.txt
	else
		time python Generators/Random.py $n $p >./Inputs/$n-$e-$p-$l-random.txt
	fi
	echo "Generated";

	echo "Genetic1-Prakhar-----------------------";
	if [ $rand -eq 0 ]
	then
		time python3 Code/ga_msp.py <./Inputs/$n-$e-$p-$l.txt
	else
		time python3 Code/ga_msp.py <./Inputs/$n-$e-$p-$l-random.txt
	fi

	echo "Genetic2-Ronak-------------------------";
	if [ $rand -eq 0 ]
	then
		time python Code/Machine.py <./Inputs/$n-$e-$p-$l.txt
	else
		time python Code/Machine.py <./Inputs/$n-$e-$p-$l-random.txt
	fi

	echo "Random & Topologically sorted----------------------------";
	if [ $rand -eq 0 ]
	then
		time python3 Code/ListShd_p.py <./Inputs/$n-$e-$p-$l.txt
	else
		time python3 Code/ListShd_p.py <./Inputs/$n-$e-$p-$l-random.txt
	fi

	echo "Swap search---------------------------";
	if [ $rand -eq 0 ]
	then
		time python Code/ListShd.py <./Inputs/$n-$e-$p-$l.txt
	else
		time python Code/ListShd.py <./Inputs/$n-$e-$p-$l-random.txt
	fi

	if [ $rand -eq 0 ]
	then
		rm ./Inputs/$n-$e-$p-$l.txt
	else
		rm ./Inputs/$n-$e-$p-$l-random.txt
	fi

done;
done;
done;
done;
	rm generate gen_dot
