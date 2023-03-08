#!/usr/bin/python3
""" Rectangle Module """
from models.base import Base
""" Import class Base """
class Rectangle(Base):
    """ Declaration of the class Rectangle that inherits from class Base
    private instance variables
    __width -> width
    __height -> height
    __x -> x
    __y -> y
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initializer """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        super().__init__(id)

    @width.setter
    def set_width(self, value):
        """setter for width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def get_width(self):
        """Returns the publicized width atribute"""
        return self.__width

    @height.setter
    def set_height(self, value):
        """setter for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def get_height(self):
        """Returns publicized height attribute """
        return self.__height

    @x.setter
    def set_x(self, value):
        """setter for x """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def get_x(self):
        """returns pulicized x atribute"""
        return Rectangle.__x

    @y.setter
    def set_y(self, value):
        """ setter for y """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @property
    def get_y(self):
        """returns publicized y attribute """
        return self.__y
