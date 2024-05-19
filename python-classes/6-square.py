#!/usr/bin/python3
"""
This module provides a class to represent a square with basic validation
and a method to calculate its area.

Classes:
    Square: A class to represent a square with a given size.
"""


class Square:
    """
    A class to represent a square.

    Attributes:
        __size (int): The size of the square's side.
        __position (tuple): The position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square instance.

        Args:
            size (int, optional): The size of the square's side. Defaults to 0.
            position (tuple, optional): The position of the square.
            Defaults to (0, 0).

        Raises:
            TypeError: If `size` is not an integer or if `position` is not a
                tuple of 2 positive integers.
            ValueError: If `size` is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square."""
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

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If `value` is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or\
           not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self._Square__size ** 2

    def my_print(self):
        """Prints a square of #.

        If size is equal to 0, prints an empty line. Otherwise, prints the
            square using '#' character.
        Adjusts the position of the square based on the position attribute.
        """
        if self._Square__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()

            for _ in range(self._Square__size):
                print(" " * self.__position[0] + "#" * self._Square__size)
