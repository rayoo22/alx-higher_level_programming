#!/usr/bin/python3

""" addition module """

def add_integer(a, b=98):
    """
    Returns an integer: the addition of a and b
    
    Args:
        a: an integer variable
        b: an integer variable
    """
    if isinstance(a, (int, float)) is not True:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)) is not True:
        raise TypeError("b must be an integer")

    return int(a + b)
