#!/usr/bin/python3
"""module
"""


class BaseGeometry():
    """BaseGeometry class
    """
    def area(self):
        """area

        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validator

        Args:
            name (str): name
            value (int): int > 0

        Raises:
            TypeError: name must be an integer
            ValueError: value must be > 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
