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
        """gets dict representation of a Student object"""
        if (type(attrs) == list and all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if (self, k)}
        return self.__dict__
