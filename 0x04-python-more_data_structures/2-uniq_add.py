#!/usr/bin/python3
def uniq_add(my_list=[]):
    number = 0
    for elem in set(my_list):
        number += elem
    return number
