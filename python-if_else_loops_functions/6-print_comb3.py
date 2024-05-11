#!/usr/bin/python3
for i in range(9):
    for j in range(i, 10):
        if i != j:
            print(i, j, sep="", end="\n" if i == 8 and j == 9 else ", ")
