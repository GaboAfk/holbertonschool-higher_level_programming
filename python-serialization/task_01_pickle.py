#!/usr/bin/python3
import pickle
"""module pickle

Returns:
    dict: pickle deserialized file
"""


class CustomObject():
    """custom object class
    """
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self.__dict__, file)

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as file:
                load = pickle.load(file)
                res = CustomObject("x", "x", False)
                for key in load:
                    setattr(res, key, load[key])
                return res
        except (FileNotFoundError, pickle.UnpicklingError):
            return None
