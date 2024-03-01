#!/usr/bin/python3
"""
Script that takes in a letter, sends a POST request,
and displays the response.
"""

import requests
import sys


if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""

    data = {'q': letter}

    response = requests.post('http://0.0.0.0:5000/search_user', data=data)

    try:
        json_response = response.json()
        if json_response:
            print("[{}] {}".format(
                json_response.get('id'),
                json_response.get('name')
            ))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
