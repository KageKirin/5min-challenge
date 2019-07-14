5 minute math challenge
=======================

simple script to challenge primary school 1st years
with simple calculus.


## Usage

The program runs on the command line. Here are its options:

```
./challenge.py --help                                                                                             ‹›
usage: challenge.py [-h] [--debug] [-t TIME] [-o {+,-,*,/,%}] [-r RANGE]
                    [--negative]

optional arguments:
  -h, --help                              show this help message and exit
  --debug                                 debug mode
  -t TIME, --time TIME                    time (min)
  -o {+,-,*,/,%}, --operation {+,-,*,/,%} operation
  -r RANGE, --range RANGE                 range
  --negative                              allow negative numbers as result
  ```

- `--debug` enables the debug mode of only 5 seconds of calculus exercises.
- `--time` sets the time (in minutes) for testing. default is 1 minute.
- `--operation='<op>'` sets the operation to test. default is addition.
  `%` is for _modulo_ operations, i.e. rest of division.
- `--range` sets the range of the operands. default is 10.
- `--negative` is for _subtraction_ operations to allow negative results.
