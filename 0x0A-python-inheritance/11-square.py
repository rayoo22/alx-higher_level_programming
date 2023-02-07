#!/usr/bin/python3
""" Square Module - inherits from Rectangle class """
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """ Definition of class Square """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ prints string """
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__, self.__size, self.__size)
