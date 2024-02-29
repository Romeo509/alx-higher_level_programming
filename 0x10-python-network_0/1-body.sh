#!/bin/bash
# This script takes a URL, sends a GET request, and displays the body of the response for a 200 status code
curl -s -X GET -i "$1" | awk '/HTTP\/1.1 200 OK/{flag=1;next}/HTTP/ && flag{exit}flag' | tail -n +2
