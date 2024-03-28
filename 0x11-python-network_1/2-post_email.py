#!/usr/bin/python3
"""
2-post_email module: takes in url and email, sends POST request
to url with email as parameter, displays body of the response
"""


import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    email = urllib.parse.urlencode({'email': sys.argv[2]}).encode('utf-8')
    request = urllib.request.Request(sys.argv[1], email)

    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))
