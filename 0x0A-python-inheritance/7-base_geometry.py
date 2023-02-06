#!/usr/bin/python3
""" BaseGeometry Class """

class BaseGeometry:
    """ Definition of BseGeometry class
        methods:
                area():raises an Exception
                integer_validator(): validates value

    """

    def area(self):
        """ not implemented """
        raise(Exception("area() is not implemented"))

    def integer_validator(self, name, value):
        """validates input 
        Args:
            name(str): assumed always a string
            value (int): greater than 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
