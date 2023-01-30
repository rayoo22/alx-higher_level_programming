#!/usr/bin/python3
"""
Rectangle module
"""

class Rectangle:
    """
    Defining Rectangle class

    """
    def __init__(self, width=0, height=0):
        """ constructor """
        self.width = width
        self.height = height
    
    @property
    def width(self):
        """ Gets the attribute to be used in class """
        return self.__width = width

    @property.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Gets the attribute to be used in class """
        return self.__height = height

    @property.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
