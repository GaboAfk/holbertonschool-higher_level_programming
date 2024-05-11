#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0:
            print("{}".format("FizzBuzz" if i % 5 == 0 else "Fizz"), end=" ")
        elif i % 5 == 0:
            print("{}".format("Buzz"), end=" ")
        else:
            print("{}".format(i), end=" ")
