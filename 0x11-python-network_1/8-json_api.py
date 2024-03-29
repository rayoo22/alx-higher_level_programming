#!/usr/bin/python3
""" """


import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        letter = ""
    else:
        letter = sys.argv[1]
    
    url = 'http://0.0.0.0:5000/search_user'
    payload = {'q': letter}
    response = requests.post(url, data=payload)

    try:
        dic = response.json()
        if dic:
            print("[{}] {}".format(dic.get('id'), dic.get('name')))
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")
