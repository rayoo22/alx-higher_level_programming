#!/bin/bash
# sends a request to URL and response body if status code is 200
display_response_body(){
	http_status=$(curl -s -o /dev/null -w "%{http_code}" "$1")

	if [ "$http_status" == "200" ]; then
		curl -s "$1"
	else
		echo "Status code: $http_status"
	fi
}
display_response_body "$1"
