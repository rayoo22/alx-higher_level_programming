#!/usr/bin/python3
"""Module 7-base_geometry"""


class BaseGeometry:
    """Has a public instnace method only"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """An integer validator
        Args:
            name: name of integer value
            value: value to be validated
        Raises:
            TypeError: if integer is not an integer
            ValueError: if value is less than 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
