#!/usr/bin/python3
"""Module 10-student"""


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
        """gets dict representation of a Student object
        Args:
            attrs: attrbutes to be represented in JSON format
        Returns:
            dictionary represention of an object
        """
        if attrs is None:
            return self.__dict__

        new_dict = {}

        for a in attrs:
            try:
                new_dict[a] = self.__dict__[a]
            except:
                pass
        return new_dict
