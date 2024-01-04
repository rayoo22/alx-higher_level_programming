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
        
    @property
    def width(self):
        """ property getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Args:
            value: sets the width attribute
        """
        if isinstance(self.__width, int) is not True:
            raise TypeError("width must be an integer")
        elif self.__width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ property getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Args:
            value: sets the height attribute
        """
        if isinstance(self.__height, int) is not True:
            raise TypeError("height must be an integer")
        elif self.__height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
