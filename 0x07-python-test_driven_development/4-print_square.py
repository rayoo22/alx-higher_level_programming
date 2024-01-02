#!/usr/bin/python3

""" Square Module """

def print_square(size):
    """

    Returns a square figure with the # character

    Args:
        size: the lenth of the square figure

    size must be an integer, otherwise raise a TypeError
    exception

    """
    if isinstance(size, int) is not True:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) is True & size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
