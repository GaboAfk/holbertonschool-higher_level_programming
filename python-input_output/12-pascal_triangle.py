#!/usr/bin/python3
"""module pascal triangle
"""


def pascal_triangle(n):
    """function to calculate triangle pascal in a list of lists

    Args:
        n (int): polynom wanted

    Returns:
        list: list of lists of integers representing the Pascal's triangle of n
    """
    if n < 0:
        return []

    res = []
    for i in range(n):
        ("i =", i)
        row = [1]
        if i > 0:
            (i, "> 0")
            pre = res[i - 1]
            ("pre =", pre)
            for j in range(1, i):
                ("j =", j)
                (f"pre[{j} - 1] + pre[{j}]")
                (pre[j - 1], "+", pre[j])
                row.append(pre[j] + pre[j - 1])
                ("append", pre[j] + pre[j - 1])
            row.append(1)
            ("append", 1)
        ("row =", row)
        res.append(row)
    return res
