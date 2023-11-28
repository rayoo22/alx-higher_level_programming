#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = list(str)

    for w in new_str:
        del new_str[n]
    print(new_str)
