#!/usr/bin/python3
""" Square class """
class Square:
    """ contents of the square class """
    def __init__(self, size=0, position=(0, 0)):
        """
        Args:
            size: size of square object created
            position: another attribute
        """
        self.__size = size
        self.__position = position

        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        
        elif all(element >= 0 for element in position) is not True:
            raise TypeError("position must be a tuple of 2 positive integers")


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
    
    @property
    def position(self):
        """
        getter: retrieves the posiotion set
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Args:
            value: position variable set
        """
        self.__position = value

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
