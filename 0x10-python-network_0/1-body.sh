#!/bin/bash
# sends a GET request to the URL, displays the body of the response
response=$(curl -s -w "%{http_code}" "$1")
body=$(echo $response | sed -e 's/[0-9]\{3\}$//')
status_code=$(echo "$response" | tail -c 4)

if [ "$status_code" -eq 200 ]; then
	echo "$body"
fi
