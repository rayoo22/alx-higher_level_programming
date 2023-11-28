#!/usr/bin/python3
for i in range(123, 96, -1):
    print("{}".format(chr(i)) if i % 2 == 0 else "{}".format(chr(i-32)), end='')
