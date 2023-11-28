#!/usr/bin/python3
def print_last_digit(number):
    last_digit = number % 10

    if number < 0:
        return -last_digit
    else:
        return last_digit
