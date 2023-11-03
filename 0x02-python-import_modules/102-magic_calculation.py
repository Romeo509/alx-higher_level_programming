#!/usr/bin/python3
def magic_calculation(a, b):
    c = 0
    if a < b:
        add = __import__('magic_calculation_102').add
        for i in range(a, b):
            c = add(c, i)
    else:
        sub = __import__('magic_calculation_102').sub
        c = sub(a, b)
    return c
