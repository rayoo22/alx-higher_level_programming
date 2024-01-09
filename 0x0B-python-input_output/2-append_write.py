#!/usr/bin/python3
"""Module 2-append_write"""


def append_write(filename="", text=""):
    """appending string at the end of filename
    Args:
        filename: file to append string to
        text: string to append at end of file
    Returns:
        number of characters added at end of file
    """
    with open(filename, mode="a", encoding="utf-8") as myFile:
        myFile.write(text)

        return len(text)            
