#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    aux_list = [0, 0]
    for i in range(2):
        if i < len_a:
            aux_list[i] += tuple_a[i]
        if i < len_b:
            aux_list[i] += tuple_b[i]
    return aux_list[0], aux_list[1]
