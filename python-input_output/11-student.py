#!/usr/bin/python3
"""student module

Returns:
    dict: dict of class student
"""


class Student():
    """student class
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        dic = self.__dict__
        return {att: dic[att] for att in attrs if att in dic}

    def reload_from_json(self, json):
        for att in json:
            setattr(self, att, json[att])
