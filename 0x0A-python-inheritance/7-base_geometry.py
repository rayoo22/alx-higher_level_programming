#!/usr/bin/python3
"""Module 7-base_geometry"""


class BaseGeometry:
    """Has a public instnace method only"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """An integer validator"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
