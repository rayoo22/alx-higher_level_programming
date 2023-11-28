#!/usr/bin/python3
for i in range(123, 96, -1):
    if i % 2 == 0:
        print(chr(i), end='')
    else:
        print(chr(i-32), end='')
