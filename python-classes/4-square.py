#!/usr/bin/python3
"""
This module provides a class to represent a square with basic validation
and a method to calculate its area.

Classes:
    Square: A class to represent a square with a given size.
"""


class Square:
    """A class to represent a square.

    Attributes:
        __size (int): The size of the square's side.
    """
    def __init__(self, size=0):
        """Initialize a Square instance.

        Args:
            size (int, optional): The size of the square's side. Defaults to 0.

        Raises:
            TypeError: If `size` is not an integer.
            ValueError: If `size` is less than 0.
        """
        self._Square__size = size

    @property
    def size(self):
        """Get the size of the square.

        Returns:
            int: The size of the square's side.
        """
        return self._Square__size
    
    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size of the square's side.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self._Square__size ** 2


my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)