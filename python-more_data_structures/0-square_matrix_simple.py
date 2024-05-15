#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    res = [list(map(lambda x: x**2, row)) for row in matrix]
    return res
