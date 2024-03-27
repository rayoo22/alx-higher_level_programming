#!/bin/bash
#takes in URL, sends DELETE request, displays the response body 
curl -sX DELETE "$1"
