#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    a, b = 0, 0
    while a < x:
        try:
            print("{:d}".format(my_list[a]), end='')
            b += 1
        except (ValueError, TypeError):
            pass
        a += 1
    print()
    return b
