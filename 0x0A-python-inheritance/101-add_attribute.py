#!/usr/bin/python3
"""Module 101-add_attribute"""


def add_attribute(obj, attr, value):
    """Adding a new attribute to an object if it possible"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add a new attribute")
    else:
        setattr(obj, attr, value)
