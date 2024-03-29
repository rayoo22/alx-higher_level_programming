#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve this challenge.
first argument will be the repository name
second argument will be the owner name
"""


import sys
import requests

if __name__ == "__main__":
    url = 'http://api.github.com/repos/{}/{}/commits'.format(sys.argv[1], sys.argv[1])
    r = requests.get(url)
    list_commits = r.json()
    for commit in list_commits[0:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
