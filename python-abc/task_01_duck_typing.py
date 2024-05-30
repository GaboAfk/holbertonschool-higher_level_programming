#!/usr/bin/python3
from abc import ABC, abstractmethod
import math


class Shape(ABC):

    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radius) -> None:
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):

    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return self.width * 2 + self.height * 2


def shape_info(Shape):
    print("Area:", Shape.area())
    print("Perimeter:", Shape.perimeter())
