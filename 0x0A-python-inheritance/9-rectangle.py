#!/usr/bin/python3

""" a new class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """ Rectangle class inheriting from BaseGeometry """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ calculates the area """
        return self.__width * self.__height

    def __str__(self):
        """ prints string """
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__, self.__width, self.__height)
