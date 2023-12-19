#!/usr/bin/python3
class Square:
    """ defines a square by size """
    def __init__(self, size=0):
        """
        object initializer

        Args:
            self: initializer for obj created
            size: attribute for square object created
        """
        self.__size = size

        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        calculates area of square object created

        Args:
            self: initializer for object created
        """
        return self.__size ** 2
