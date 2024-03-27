#!/bin/bash
# takes in URL, send s request to URL, displays size of
# body of the response
response_size=$(curl -s "$1" | wc -c)
echo "$response_size"
