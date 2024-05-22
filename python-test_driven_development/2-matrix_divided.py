#!/usr/bin/python3
"""
    matrix module
"""


def matrix_divided(matrix, div):
    """matrix function, use div to divide list of lists

    Args:
        matrix (list of list): list of list of elements
        div (int or float): divisor

    Raises:
        TypeError: matrix must be a matrix (list of lists)\
                                of integers/floats
        TypeError: Each row of the matrix must have the same size
        TypeError: div must be a number
        ZeroDivisionError: division by zero

    Returns:
        matrix(list of lists): list of lists divided by div rounded by 2 dec
    """
    if not all(isinstance(elem, (int, float))
       for row in matrix for elem in row):
        raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
    if not all(len(matrix[0]) == len(row) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(elem / div, 2) for elem in row] for row in matrix]
