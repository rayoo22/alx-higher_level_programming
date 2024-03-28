#!/usr/bin/python3
"""
1-hbtn_header module
"""


import sys
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(f"{sys.argv[1]}") as response:
        x_request_id = response.headers.get('X-Request-ID')
        print(x_request_id)
