#!/usr/bin/python3
""" Only sub class of """
def inherits_from(obj, a_class):
    """ to get where the object is inheriting from """
    return ((type(obj) != a_class) and issubclass(type(obj), a_class)) 
