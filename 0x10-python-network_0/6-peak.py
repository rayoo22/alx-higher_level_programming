#!/usr/bin/python3
"""
function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    function: find_peak
    Args: list_of_integers
    """
    list_of_integers.sort()

    number_of_elements = len(list_of_integers)
    
    for i in list_of_integers:
        return list_of_integers[number_of_elements - 1]
