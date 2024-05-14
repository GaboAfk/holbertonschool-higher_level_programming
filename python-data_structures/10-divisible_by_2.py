#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    res = []
    for i in range(len(my_list)):
        res.append(my_list[i] % 2 == 0)
    return res
