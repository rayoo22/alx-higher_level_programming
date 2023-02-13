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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        super().__init__(id)

        @property
        def set_width(self, width):
            """setter for width """
            Rectangle.__width = width

        @width.property
        def get_width(self):
            """Returns the publicized width atribute"""
            return Rectangle.__width

        @property
        def set_height(self, height):
            """setter for height"""
            Rectangle.__height = height

        @height.property
        def get_height(self):
            """Returns publicized height attribute """
            return Rectangle.__height

        @property
        def set_x(self, x):
            """setter for x """
            Rectangle.__x = x

        @x.property
        def get_x(self):
            """returns pulicized x atribute"""
            return Rectangle.__x

        @property
        def set_y(self, y):
            """ setter for y """
            Rectangle.__y = y

        @y.property
        def get_y(self):
            """returns publicized y attribute """
            return Rectangle.__y

