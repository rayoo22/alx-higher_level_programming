#!/usr/bin/python3
for ch in range(97, 123):
    if ch in [101, 113]:
        continue
    print("{}".format(chr(ch)), end='')
