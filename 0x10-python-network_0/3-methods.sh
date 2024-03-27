#!/bin/bash
# takes in a URL, displays all http methodsthe server will accept
curl -sI "$1" | grep 'Allow:' | cut -f2- -d' '
