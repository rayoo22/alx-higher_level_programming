#!/usr/bin/python3
""" The Rectangle Module
"""


class Rectangle:
    """
    The Rectangle class

    Args:
        width: the width of the retangle
        height: the height of the rectangle

    Attributes:
        width: width of rectangle
        height: height of rectangle
    """
    
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        
        if isinstance(width, int) is not True:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")

        if isinstance(height, int) is not True:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    def area(self):
        """
        Args:
            width: width of the rectangle obj
            height: height of the rectangle obj

        Returns:
            The area of the rectangle
        """
        area = self.__width * self.__height
        return area

    def perimeter(self):
        """
        Args:
            width: width of the rectangle obj
            height: height of the rectangle obj

        Returns:
            The perimeter of the rectangle obj
        """
        if self.__width == 0 | self.__height == 0:
            perimeter = 0

        perimeter = (self.__width + self.__height) * 2
        return perimeter
