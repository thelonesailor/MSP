#!/bin/bash
	g++ -O3 -std=c++11 -o generate rgpos.cpp
	g++ -O3 -std=c++11 -o gen_dot gen_dot.cpp


for n in {100..100};
do
for e in 240; # ((e=$n-1;e<=2*$n;e+=20));
do
for p in 10;
do
for l in 1000;
do

	echo "Generating n=$n e=$e p=$p l=$l";
	time ./generate $n $e $p $l > ./Inputs/$n-$e-$p-$l.txt
	# time python Random.py >./Inputs/$n-$e-$p-$l-random.txt
	# time ./gen_dot $p >./Inputs/$n-$e-$p-$l.txt
	echo "Generated";	


	echo "Genetic1-Prakhar-----------------------";
	time python3 ga_msp.py <./Inputs/$n-$e-$p-$l.txt
	# time python3 ga_msp.py <./Inputs/$n-$e-$p-$l-random.txt

	
	echo "Genetic2-Ronak-------------------------";
	time python Machine.py <./Inputs/$n-$e-$p-$l.txt
	# time python Machine.py <./Inputs/$n-$e-$p-$l-random.txt


	echo "Random & Topologically sorted----------------------------";
	time python3 ListShd_p.py <./Inputs/$n-$e-$p-$l.txt
	# time python3 ListShd_p.py <./Inputs/$n-$e-$p-$l-random.txt


	echo "Swap search---------------------------";
	time python ListShd.py <./Inputs/$n-$e-$p-$l.txt	
	# time python ListShd.py <./Inputs/$n-$e-$p-$l-random.txt
	
done;
done;
done;
done;
	rm generate gen_dot