#!/usr/bin/python3

""" Say_my_name module """

def say_my_name(first_name, last_name=""):
    
    """
    Returns: The statement 'My name is <first name> <last name>'

    Args:
        first_name: the first name
        last_name: the last name

    Raises an exception if variables are not strings
    """
    if isinstance(first_name, str) is not True:
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str) is not True:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
