#!/bin/bash
# script to send request to URL, as an arg,
# displays status code of response
curl -sI -w '%{response_code}' "$1" -o /dev/null
