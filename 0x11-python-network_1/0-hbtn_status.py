#!/usr/bin/python3
"""
0-hbtn_status module
"""


import urllib.request

if __name__ == "__main__":
    """
    fetches 'https://alx-intranet.hbtn.io/status
    """
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        html = response.read()
