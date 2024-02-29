#!/bin/bash
# This script makes a request to 0.0.0.0:5000/catch_me and causes the server to respond with "You got me!"
curl -s -X PUT -d "user_id=98" 0.0.0.0:5000/catch_me -w "You got me!\n"
