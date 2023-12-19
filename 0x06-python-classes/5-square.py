#!/usr/bin/python3
""" Square class """
class Square:
    """ contents of the square class """
    def __init__(self, size=0):
        """
        Args:
            size: size of square object created
        """
        self.__size = size

        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
    
    @property
    def size(self):
        """
        getter : retrieves the size set
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ 
        Args:
            value: variable to be set
        """
        self.__size = value

    def area(self):
        """ 
        calcultes area of square

        Returns:
            area of square
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints square using #
        """
        if self.__size == 0:
            print('\n', end='')
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()
