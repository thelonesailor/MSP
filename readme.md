# Solving Multiprocessor Scheduling Problem

Following 4 files can solve the Multiprocessor scheduling problem:
* `ga_msp.py`
* `Machine.py`
* `ListShd_p.py`
* `ListShd.py`


Best results were found with `ListShd.py`, to run these files use:
```
	python3 Code/ga_msp.py     < input  > output
	python  Code/Machine.py    < input  > output
	python3 Code/ListShd_p.py  < input  > output
	python  Code/ListShd.py    < input  > output
```
`input` should have format specified by `input_format.md`

`output` will have the time taken by best schedule found.


[Link for project report](https://docs.google.com/document/d/14DJq7WXIiWILgJ9qX0H9KeC6FdyP2yvbG1UfvLXwZxI/edit?usp=sharing)

[Link for test cases used](http://www.kasahara.elec.waseda.ac.jp/schedule/stgarc_e.html)

[Paper for Genetic Algorithm](http://ieeexplore.ieee.org/document/265940/)

[Paper for List Scheduling](http://ieeexplore.ieee.org/document/6767827/)

### Using scripts

* Running `./convert.sh` will take test cases from folders `50 and 100` convert format and output them in `Inputs` folder.

* `e1.sh`,`e2.sh`,`e3.sh`,`e4.sh` will run `ga_msp.py`,`Machine.py`,`ListShd_p.py`,`ListShd.py` on testcases in `Inputs` folder and output results in `Result_files` folder.

* `eold.sh` will generate input file from one of file in Generators and run all 4 above files on the input file.

* `a.sh` reads the files in `Result_files` and optimal times from `Optimal_values` and outputs the average percentage above optimal values in `Result_files/RESULT.txt`
