#!/usr/bin/python3
"""Module 1-my_list"""


class MyList(list):
    """MyList class that inherits from the list class"""
    def print_sorted(self):
        """Prints a sorted list"""
        return self.sort()
