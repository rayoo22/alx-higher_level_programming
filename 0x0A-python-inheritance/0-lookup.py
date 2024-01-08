#!/usr/bin/python3
"""Module 0-lookup"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object
    Args:
        obj: object to check its attributes and methods
    """
    return dir(obj)
