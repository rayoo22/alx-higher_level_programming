#!/usr/bin/python3
""" Square Module
    Inherits from Rectangle Class """
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """ Definition of Square Class """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
