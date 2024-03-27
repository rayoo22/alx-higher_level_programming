#!/bin/bash
# takes in URL, send s request to URL, displays size of
# body of the response
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
