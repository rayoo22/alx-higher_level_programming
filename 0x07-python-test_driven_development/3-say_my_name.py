#!/usr/bin/python3

def say_my_name(first_name, last_name=""):

    if (isinstance(first_name, str)) == True:
        if (isinstance(last_name, str)) == True:
            print(f"My name is {first_name} {last_name}")
    else:
        print("

