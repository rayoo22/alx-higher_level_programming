#!/usr/bin/python3
""" Square module """

class Square:
    """ Declares a Square class """

    def __int__(self, size=0) -> None:
        """
        Initializes class attributes
        Args:
        size: size of square
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size mus be >= 0")
        else:
            self.__size = size
