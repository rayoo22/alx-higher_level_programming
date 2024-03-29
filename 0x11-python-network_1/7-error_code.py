#!/usr/bin/python3
"""
 takes in a URL, sends a request to the URL and displays the body of the response.
 If the HTTP status code is greater than or equal to 400, print: Error code: followed by the value of the HTTP status code
"""


import requests
import sys

if __name__ == "__main__":
    try:
        reponse = requests.get(sys.argv[1])
        response.raise_for_status()
        print(response.text)
    except:
        print("Error code: {}".format(response.status_code))
