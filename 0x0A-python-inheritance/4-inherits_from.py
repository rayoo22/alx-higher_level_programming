#!/usr/bin/python3
"""Module 4-inherits_from"""


def inherits_from(obj, a_class):
    """checks if obj is an instance of a class or a subclass
    Args:
        obj: object to check its parent derivation
        a_class: subclass to check whether obj comes from it
    Returns:
        True if obj is an instance of a_class (subclass), otherwise False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
