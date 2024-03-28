#!/usr/bin/python3
"""
4-hbtn_status module
"""


import sys
import urllib.request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    request = urllib.request.Request(url)
    
    with urllib.request.urlopen(request) as response:
        body = response.read().decode('utf-8')
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
