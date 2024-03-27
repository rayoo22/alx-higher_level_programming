#!/bin/bash
# Takes in URL, add header variable, displays Hello School!
curl -s -H "X-School-User-Id":98 "$1"
