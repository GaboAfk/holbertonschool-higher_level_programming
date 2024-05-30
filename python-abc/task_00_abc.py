#!/usr/bin/python3
"""module

Returns:
    str: Animal Sound
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Animal Class

    Args:
        ABC (any): abstract
    """

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """Dog Animal SubClass

    Args:
        Animal (any): Dogs
    """
    def sound(self):
        return "Bark"


class Cat(Animal):
    """Cat Animal SubClass

    Args:
        Animal (any): Cats
    """
    def sound(self):
        return "Meow"
