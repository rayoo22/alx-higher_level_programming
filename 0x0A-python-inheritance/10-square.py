#!/usr/bin/python3
""" Square Module """

class Square(Rectangle):
    """ Defining of the Square class """
    def __init__(self, size):
        self.__size = size
        super().integer_validator("size", size)

    def area():
        return self.__size * self.__size
