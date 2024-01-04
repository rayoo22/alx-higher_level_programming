#!/usr/bin/python3
"""The Rectangle Module"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """
        Args:
            width: width of rectangle object
            height: height of rectangle object
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """property getter"""
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(self.__width, int) is not True:
            raise TypeError("width must be an integer")
        elif self.__width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """property getter"""
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(self.__height, int) is not True:
            raise TypeError("height must be an integer")
        elif self.__height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns area of rectangle"""
        area = self.__width * self.__height
        return area

    def perimeter(self):
        """ Returns the perimeter of rectangle object """
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        else:
            perimeter = (self.__width + self.__height) * 2

        return perimeter

    def __str__(self):
        """printing string representation of rectangle"""
        return '\n'.join('#' * self.__width for _ in range(self.__height))
