#!/usr/bin/python3
"""module Square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square inherits from Rectangle

    Args:
        Rectangle (BaseGeometry): size
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
