#!/usr/bin/python3
""" Module 1-write_file """


def write_file(filename="", text=""):
    """function writing a string to file
    Args:
        filename: file to write to
        text: string to write in filename
    Returns:
        The number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as myFile:
        myFile.write(text)

    with open(filename, encoding="utf-8") as myFile:
        readtext = myFile.read()
        
        count = 0

        wordlist = readtext.split()

        for word in wordlist:
            for char in word:
                 count += 1
    return count
