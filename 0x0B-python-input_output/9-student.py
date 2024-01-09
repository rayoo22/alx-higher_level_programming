#!/usr/bin/python3
"""Module 9-student"""


class Student:
    """class Student
    Args:
        first_name: their fist name
        last_name: their last name
        age: their age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        if isinstance(self, (str, int, bool)):
                return self
        elif isinstance(self, dict):
            return {key: Student.to_json(value) for key, value in self.items()}
        elif isinstance(self, list):
            return [Student.to_json(item) for item in self]
        elif hasattr(self, '__dict__'):
            return Student.to_json(self.__dict__)
