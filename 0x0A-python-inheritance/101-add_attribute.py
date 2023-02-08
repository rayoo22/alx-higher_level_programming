#!/usr/bin/python3
""" Module 101-add_attribute """

def add_attribute(obj, attribute, value):
    """ function that adds an attribute if it is possible """
    if ('__dict__' in dir(obj)):
        setattr(obj, attribute, value)

    else:
        raise TypeError("cant add new attribute")
