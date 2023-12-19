#!/usr/bin/python3
""" class Square """
class Square:
    """ defines a square by size """
    def __init__(self, size=0):
        """
        object initializer

        Args:
            self: for object created
            size: attribute for the object created
        """
        self.__size = size

        if not type(size) is int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
