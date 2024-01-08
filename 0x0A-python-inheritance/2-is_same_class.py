#!/usr/bin/python3
"""Module 2-is_same_class"""


def is_same_class(obj, a_class):
    """checks if obj is an instance of a_class
    Args:
        obj: object to check
        a_class: parent class of obj

    Returns:
        True if obj is an instance of a_class, otherwise False
    """
    if isinstance(obj, a_class) is True:
        return True
    else:
        return False
