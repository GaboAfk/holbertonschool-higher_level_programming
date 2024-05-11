#!/usr/bin/python3
def print_last_digit(number):
    res = abs(number) % 10
    print("{}".format(res), end="")
    return res
