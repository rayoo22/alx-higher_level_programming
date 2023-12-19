#!/usr/bin/python3
class Square:
    """ defines a square by size """
    def __init__(self, size=0):
        """ private instance variable """
        self.__size = size

        if not type(size) is int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2
