#!/usr/bin/python3

for tens_digit in range(10):
    for ones_digit in range(tens_digit + 1, 10):
        if tens_digit < 9:
            print("{:d}{:d}, ".format(tens_digit, ones_digit), end='')
        else:
            print("{:d}{:d}".format(tens_digit, ones_digit))

print()  # To add a newline at the end of the output
