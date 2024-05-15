#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    res = {}
    for key, value in a_dictionary.items():
        res[key] = value*2
    return res
