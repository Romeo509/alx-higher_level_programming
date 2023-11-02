#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    arg_digit = len(argv) - 1
    if arg_digit == 0:
        print("{}".format(arg_digit))
    else:
        result = []
        for i in range(1, arg_digit + 1):
            result.append(int(argv[i]))
        print("{}".format(sum(result)))
