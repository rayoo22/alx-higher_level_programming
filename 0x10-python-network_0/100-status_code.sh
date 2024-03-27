#!/bin/bash
# script to send request to URL, as an arg,
# displays status code of response
curl -s -o /dev/null -w "%{http_code}" "$1"
