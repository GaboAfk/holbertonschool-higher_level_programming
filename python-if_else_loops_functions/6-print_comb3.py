#!/usr/bin/python3
for i in range(9):
    for j in range(i, 10):
        if i != j:
            print("{}{}".format(i, j), end="\n" if i == 8 and j == 9 else ", ")
