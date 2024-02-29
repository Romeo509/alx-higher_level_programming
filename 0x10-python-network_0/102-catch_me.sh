#!/bin/bash
# This script makes a request to 0.0.0.0:5000/catch_me and causes the server to respond with "You got me!"
curl -s -X PUT -L -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me -L -H "User-Agent:HolbertonSchool" -L -G

