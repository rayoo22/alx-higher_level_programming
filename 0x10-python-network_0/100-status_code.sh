#!/bin/bash
# script to send request to URL, as an arg,
# displays status code of response
curl -o /dev/null -w '%{http_code}' -sLI "$1"
