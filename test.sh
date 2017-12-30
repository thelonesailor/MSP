mkdir -p ./Result_test
mkdir -p ./Result_test/genetic1
mkdir -p ./Result_test/genetic2
mkdir -p ./Result_test/randtop
mkdir -p ./Result_test/swapsearch
time ./e1.sh 0 0 &
time ./e2.sh 0 0 &
time ./e3.sh 0 0 &
time ./e4.sh 0 0 &
time ./a.sh &
time ./convert.sh &
time ./eold.sh 0 &
time ./eold.sh 1 &
time ./eold.sh 2 &
wait
rm -rf Result_test

# To actually run
# time ./e1.sh 91527 179 &
# time ./e2.sh 91527 179 &
# time ./e3.sh 91527 179 &
# time ./e4.sh 91527 179 &
# wait
