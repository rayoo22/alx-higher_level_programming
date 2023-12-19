#!/usr/bin/python3
class Square:
    """ defines a square by size """
    def __init__(self, size=0):
        """ Initializer, private instance variable """
        self.__size = size

        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
    
    @property
    def size(self):
        """ getter """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter """
        self.__size = value

    def area(self):
        """ area of square """
        return self.__size ** 2
