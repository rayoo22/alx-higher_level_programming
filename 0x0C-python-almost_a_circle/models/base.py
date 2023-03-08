#!/usr/bin/python3
""" Base Module """

class Base():
    """
    __nb_objects: private class attribute
    def __init__(self, id=None): class constructor
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize id, increment class attribute if no id is set as id """
        if id:
            self.id = id

        Base.__nb_objects += 1
        self.id = Base.__nb_objects
