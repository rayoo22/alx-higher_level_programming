#!/usr/bin/python3
"""Module 7-base_geometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """instantiation for subclass Rectangle
    Args:
        width: private instance variable
        height: private instance variable
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

        super().integer_validator("width", width)
        super().integer_validator("height", height)
