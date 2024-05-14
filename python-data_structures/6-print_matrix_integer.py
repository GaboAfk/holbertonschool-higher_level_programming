#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    len_i = len(matrix)
    for i in range(len_i):
        len_j = len(matrix[i])
        for j in range(len_j):
            print("{:d}".format(matrix[i][j]), end='')
            if j != len_j-1:
                print(end=' ')
        print()
