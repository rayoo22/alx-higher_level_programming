#!/usr/bin/python3
""" a new class """
class Rectangle(BaseGeometry):
    """ Rectangle class inheriting from BaseGeometry """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
