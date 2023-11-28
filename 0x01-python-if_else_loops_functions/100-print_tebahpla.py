#!/usr/bin/python3
for i in range(0, 26):
    word = ord('z') - i
    if (i % 2 == 1):
        word = chr(word - ord('a') + ord('A'))
    else:
        word = chr(word)
    print("{}".format(word), end='')
