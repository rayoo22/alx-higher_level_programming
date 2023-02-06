#!/usr/bin/python3
""" MyList Module """

class MyList(list):
    """ Declaration of MyList class
        
        methods:
            print_sorted(): prints ascending sorted list
    """
    def print_sorted(self):
        """ prints a sorted list """

        print(sorted(self))
