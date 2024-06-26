#!/usr/bin/python3
"""module rectangle"""


class Rectangle():
    """Rectangle class declaration"""

    def __init__(self, width=0, height=0):
        """Rectangle constructor

        Args:
            width (int, optional): width of rectangle. Defaults to 0.
            height (int, optional): height of rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """get width of the rectangle

        Returns:
            int: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """set rectangle width

        Args:
            value (int): width

        Raises:
            TypeError: must be an int
            ValueError: must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get rectangle height

        Returns:
            int: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """set rectangle height

        Args:
            value (int): heigth

        Raises:
            TypeError: must be an int
            ValueError: must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """rectangle area

        Returns:
            int: area
        """
        return self.__height * self.__width

    def perimeter(self):
        """rectangle perimeter

        Returns:
            int: perimeter, if a side is 0 return 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__height * 2 + self.__width * 2
