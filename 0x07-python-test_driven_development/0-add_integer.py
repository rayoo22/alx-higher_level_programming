#!/usr/bin/python3
""" contains an add_integer function for project """

def add_integer(a, b=98):
    """ computes the sum of two integers.
    Args:
        a (int): The first number.
        b (int, optional): Thhe second number.
    Return:
        int: The sum of the two integers.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    else:
        return (int(a) + int(b))
