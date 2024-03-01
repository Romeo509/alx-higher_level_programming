#!/usr/bin/python3
"""
Script that takes in a URL and an email, sends a POST request, and displays the body of the response.
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Data to be sent in the POST request
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # Make the POST request
    with urllib.request.urlopen(url, data=data) as response:
        body = response.read().decode('utf-8')
        print("Your email is: {}".format(email))
        print(body)
