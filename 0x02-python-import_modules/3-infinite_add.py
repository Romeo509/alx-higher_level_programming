#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    num_args = len(sys.argv) - 1
    if num_args == 0:
        print("0")
    elif num_args > 0:
        total = sum(int(arg) for arg in sys.argv[1:])
        print("{}".format(total))
