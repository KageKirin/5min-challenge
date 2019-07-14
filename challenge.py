#! /usr/bin/env python3

import os, sys, time, random, argparse


def create_exercise(args):
    a = random.randint(0, args.range)
    b = random.randint(0, args.range)
    if args.operation == '-' and not args.negative:
        a = random.randint(b, args.range)
    if args.operation == '/' or args.operation == '%':
        b = random.randint(1, args.range)
    
    return "{} {} {}".format(a, args.operation, b)

def eval_exercise(computation, result):
    rr = int(eval(computation))
    print(rr)
    if rr == int(result):
        return True
    return False

def main(args):
    count_exe = 0
    count_good = 0
    count_bad = 0

    end_timer = time.time() + args.time * 60
    if args.debug:
        end_timer = time.time() + 5

    while time.time() < end_timer:
        count_exe += 1
        exe = create_exercise(args)
        result = input(exe + ' = ') or 0
        ok = eval_exercise(exe, result)
        if ok:
            count_good += 1
        else:
            count_bad += 1
        print('👍' if ok else '👎')
    
    print("exercises:", count_exe)
    print("👍:", count_good, "/", count_exe)
    print("👎:", count_bad, "/", count_exe)
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', help='debug mode', action='store_true')
    parser.add_argument('-t', '--time', help='time (min)', type=int, default=1)
    parser.add_argument('-o', '--operation', help='operation', choices=['+', '-', '*', '/', '%'], type=str, default='+')
    parser.add_argument('-r', '--range', help='range', type=int, default=10)
    parser.add_argument('--negative', help='allow negatives', action='store_true')
    args = parser.parse_args()
    random.seed()
    main(args)