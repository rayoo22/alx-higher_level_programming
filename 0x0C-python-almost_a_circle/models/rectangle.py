#!/usr/bin/python3
""" Module rectangle.py """
import sys
from models.base import Base


class Rectangle(Base):
    """ class Rectangle inheriting from class Base
    Args:
        width: width of rectangle
        height: height of rectangle
        x: instance variable
        y: instance variable
        id: instance variable
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """getter function for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if type(self.__width) != int:
            raise TypeError("width must be an integer")
        elif self.__width <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """getter function for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if type(self.__height) != int:
            raise TypeError("height must be an integer")
        elif self.__height <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(self.__x) is not int:
            raise TypeError("x must be an integer")
        elif self.__x < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(self.__y) is not int:
            raise TypeError("y must be an integer")
        elif self.__y < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """Returns the area value of the rectangle instance
        Takes width and height as arguments
        """
        return self.__width * self.__height

    def display(self):
        """prints to stdout the Rectangle object creates
        using the character '#'
        """
        print("\n" * self.__y +
                "\n".join(" " * self.__x + "#" * self.__width
                    for i in range(self.__height)))

    def __str__(self):
        """string representation of the object created"""
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id,
                self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """uses args to print non-keyworded arguments and
        kwargs to print keyworded arguments"""
        if args:
            for k, v in enumerate(args):
                if k == 0:
                    self.id = v
                elif k == 1:
                    self.width = v
                elif k == 2:
                    self.height = v
                elif k == 3:
                    self.x = v
                else:
                    self.y = v
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """returning dictionary representation of rectangle object"""
        return {"id": self.id, "width": self.width,
                "height": self.height, "x": self.x, "y": self.y
                }
