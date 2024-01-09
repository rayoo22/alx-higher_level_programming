#!/usr/bin/python3
"""Module 0-read_file"""


def read_file(filename=""):
    """function that reads a text file(UTF-8)
    Args:
        filename: file to read from
    """
    with open(filename, 'r', encoding='utf-8') as myFile:
        print(myFile.read(), end="")
