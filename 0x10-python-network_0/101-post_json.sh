#!/bin/bash
# This script sends a JSON POST request to a URL with the contents of a file as the body
curl -s "$1" -d "@$2" -H POST -X "Content-Type: application/json"
