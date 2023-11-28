#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        x = ord(str[i])
        if x >= 97 and x <= 112:
            x = x - 32
        y = chr(x)
        print("{}".format(y), end=' ')
