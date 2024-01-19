#!/usr/bin/python3
"""square module, inheriting from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ inheriting from Rectangle module"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializing the square class
        using attribute arrangement of previous
        class in this subclass"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter for the size of square"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for the size of square
        after inheritance, the size of the square
        is given the value of the width or height of
        rectangle class"""
        self.width = value
        self.height = value

    def __str__(self):
        """string representation of the object"""
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """update for args and kwargs"""
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """returning the dictionary representation of the square
        object"""
        return {'id': self.id, 'size':self.size, 'x': self.x,
                'y': self.y}
