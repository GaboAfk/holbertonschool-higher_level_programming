#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of", number, "is", end=" ")
last = number % 10
if number < 0 and not last == 0:
	last -= 10
print(last, end=" ")
if last > 5:
	print("and is greater than 5")
elif last == 0:
	print("and is 0")
else:
	print("and is less than 6 and not 0")
