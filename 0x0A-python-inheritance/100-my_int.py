#!/usr/bin/python3
""" MyInt Module """
class MyInt(int):
    """ declaration of class Myint inherited from class int """
    def __init__(self, num):
        self.num = num

    def __eq__(self, other):
        return self.num != other

    def __ne__(self, other):
        return self.num == other
