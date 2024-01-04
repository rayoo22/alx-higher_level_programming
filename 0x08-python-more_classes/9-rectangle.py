#!/usr/bin/python3
""" The Rectangle Module
"""


class Rectangle:
    """ Rectangle class """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Args:
            width: width of rectangle object
            height: height of rectangle object
        """
        self.__width = width
        self.__height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ property getter """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Args:
            value: property setter
        """
        if isinstance(self.__width, int) is not True:
            raise TypeError("width must be an integer")
        elif self.__width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ property getter """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Args:
           value: property setter
        """
        if isinstance(self.__height, int) is not True:
            raise TypeError("height must be an integer")
        elif self.__height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Returns: area of rectangle """
        area = self.__width * self.__height
        return area

    def perimeter(self):
        """ Returns the perimeter of rectangle object """
        if self.__width == 0 | self.__height == 0:
            perimeter = 0
        else:
            perimeter = (self.__width + self.__height) * 2

        return perimeter

    def __str__(self):
        """ printing string representation of rectangle """
        if width == 0 | height == 0:
            return ""

        return '\n'.join(Rectangle.print_symbol * self.__width for _ in range(self.__height))

    def __repr__(self):
        """ prints formal str representation of rectangle """
        return "Rectangle ({}, {})".format(self.__width, self.__height)
    def __del__(self):
        """ deltes rectangle object """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """
        Args:
            rect_1: an object of Rectangle class
            rect_2: an object of Rectangle class

        Returns:
            The biggest rectangle object, based on their area()
        """

        if isinstance(rect_1, Rectangle) is not True:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is not True:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1

        else:
            if rect_1.area() >= rect_2.area():
                return rect_1
            else:
                return rect_2
