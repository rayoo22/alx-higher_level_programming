#!/usr/bin/python3
"""
Square Module
"""
class Square:
    """
    class definition
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """
        getter for size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter: sets value to size
        """
        if isinstance(value, int) is not True:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates area of square
        Returns:
            area
        """
        return (self.__size) ** 2

    def __eq__(self, other):
        """
        compares and returns if equal
        """
        return self.size == other.size
    
    def __ne__(self, other):
        """
        compares and returns if mot equal
        """
        return self.size < other.size

    def __le__(self, other):
        """
        compares and returns if lesser than or equal to
        """
        return self.size <= other.size

    def __gt__(self, other):
        """
        compares and returns if greater than
        """
        return self.size > other.size

    def __ge__(self, other):
        """
        compare and returns if greater than or equal to
        """
        return self.size >= other.size
