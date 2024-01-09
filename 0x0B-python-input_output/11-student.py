#!/usr/bin/python3
"""Module 11-student"""


class Student:
    """class Student
    Args:
        first_name: their fist name
        last_name: their last name
        age: their age
    """
    def __init__(self, first_name, last_name, age):
        """Initialization of class attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """gets dict representation of a Student object"""
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for a in attrs:
            try:
                new_dict[a] = self.__dict__[a]
            except:
                pass
        return new_dict

    def reload_from_json(self, json):
        """replaces all attributes of the student instance
        Args:
            json: format holding th instance attributes
        """
        for key in json:
            try:
                setattr(self, key,json[key])
            except:
                pass
