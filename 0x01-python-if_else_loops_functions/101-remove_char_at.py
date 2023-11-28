#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = str
    if (str):
        str = str[:n] + str[n + 1:]
    if (n < 0):
        str = new_str
    return (str)
