#!/usr/bin/python3
"""Module 3-is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """checks if obj is an instance of, or if obj is an 
    instance of a class that inherited from
    Args:
        obj: instace to check its derivation
        a_class: class or inherited class to check instance derivation
    Returns:
        True if obj is an instnace of a_class or 
        inherited class of a_class, otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
