#!/usr/bin/python3
"""Module 101-add_attribute"""


def add_attribute(obj, attr, value):
    """Adding a new attribute to an object if it possible
    Args:
        obj: instance instantiated from a class
        attr: attribute to be added
        value: value of the attribute added
    Raises:
        TypeError: error that attribute can't be added
    Returns:
        returns a newly set attribute to an object
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add a new attribute")
    else:
        setattr(obj, attr, value)
