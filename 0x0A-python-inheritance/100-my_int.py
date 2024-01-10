#!/usr/bin/python3
"""Module 100-my_int.py"""


class MyInt(int):
    """inverts int operators == and !="""

    def __eq__(self, value):
        """Overide '==' operator with '!=' behaviour"""
        return self.real != value

    def __ne__(self, value):
        """ overide != operator with == behaviour"""
        return self.real == value
