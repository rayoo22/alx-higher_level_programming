#!/usr/bin/python3
"""Module 10-square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """instantiation for subclass Square
    Args:
        size: private instance variable
    """
    def __init__(self, size):
        self.__size = size

        super().integer_validator("size", size)

    def area(self):
        """implementing area() for Rectangle class"""
        area = self.__size * self.__size
        return area

    def __str__(self):
        """string representation of class attributes"""
        return '[Rectangle] {}/{}'.format(self.__size, self.__size)
