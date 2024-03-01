#!/usr/bin/python3
"""
Script that takes in a URL, sends a request, and display
the value of the X-Resquest-Id variable in the header.
"""


import urllib.request
import sys

if __name__ == "_main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        x_request_id = response.header.get('X-Request-Id')
        print(X_request_id)
