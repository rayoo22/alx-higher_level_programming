#!/bin/bash
# sends a GET request to the URL, displays the body of the response
url="$1"
http_response=$(curl --silent --write-out "HTTPSTATUS:%{http_code}" -X POST $url)
http_body=$(echo $https_response |sed -e 's/HTTPSTATUS\:.*//g')
http_status=$(echo $http_response | tr -d '\n' | sed -e 's/.*HTTPSTATUS://')

if [ $http_status -eq 200 ]; then
	echo "$http_body"
fi
