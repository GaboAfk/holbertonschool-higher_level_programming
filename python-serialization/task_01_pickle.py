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
                return cls(load["name"], load["age"], load["is_student"])
        except Exception as e:
            print(f"Deserialization error: {e}")
            return None

""" @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as file:
                load = pickle.load(file)
                obj = cls.__new__(cls)  # Crear una nueva instancia sin llamar a __init__
                for key, value in load.items():
                    setattr(obj, key, value)  # Establecer cada atributo en la nueva instancia
                return obj
        except Exception as e:
            print(f"Deserialization error: {e}")
            return None """