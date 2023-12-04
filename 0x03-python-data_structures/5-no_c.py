#!/usr/bin/python3
def no_c(my_string):
    rem = 'c'
    rem1 = 'C'
    new_string = ""

    for i in my_string:
        if i != rem and i != rem1:
            new_string += i
    res = new_string
    return res
