#!/bin/bash
# takes in url, sends request to URL, displays size of body of response
curl -s "$1" | wc -c
