#!/bin/bash
# This script takes a URL and displays all HTTP methods the server will accept
curl -sI -X OPTIONS "$1" | grep -i Allow | cut -d' ' -f2-
