#!/usr/bin/python3
"""Module 100-append_after"""


def append_after(filename="", search_string="", new_string=""):
    """searches and updates"""
    read = []
    with open(filename, "r", encoding="utf-8") as myFile:
        read = myFile.readlines()
        index = 0

        while index < len(read):
            if search_string is read[index]:
                read[index:index + 1] = [read[index], new_string]
                index += 1
            index += 1

    with open(filename, "w", encoding="utf-8") as myFile:
        myFile.writelines(read)
