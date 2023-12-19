#!/usr/bin/python3
""" the Square module """
class Square:
    """ definition of the Square clas """
    def __init__(self, size=0, position=(0, 0)):
        """
        Args:
            size: size of the square object
            position: a tuple for the square object
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        a getter for the variable size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter for all Square objects created
        Args:
            value: set value for size variable
        """
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = value
    
    @property
    def position(self):
        """
        getter for the tuple position
        """
        return self.__position
    @position.setter
    def position(self, value):
        """
        setter for all square objects created
        Args:
            value: set value for the position variable
        """
        if all(element >= 0 for element in position) is not True:
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """
        Calculates the area of the area object created
        """
        return int(self.__size) ** 2

    def my_print(self):
        """
        prints square with #
        """
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            print("\n". join([" " * self.__position[0] +
                            "#" * self.__size
                            for rows in rane(self.__size)]))

    def __str__(self):
        """
        string representation of square print call works
        Example: print(my_square)
        """
        string = ""
        if self.__size == 0:
            return string

        string += "\n" * self.position[1]
        string += "\n".join([" " * self.__position[0] +
                            "#" * self.__size
                            for rows in range(self.__size)])
        return string
