#!/usr/bin/python3
def uppercase(str):
    res = ""
    for i in str:
        if 'a' <= i <= 'z':
            res += chr(ord(i) - 32)
        else:
            res += i
    print("{}".format(res))
