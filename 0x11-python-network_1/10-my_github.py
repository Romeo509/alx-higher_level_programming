#!/usr/bin/python3
"""
Script that takes GitHub credentials
(username and personal access token),
uses the GitHub API to display the user's id.
"""


import requests
from sys import argv

if __name__ == '__main__':
    username = argv[1]
    access_token = argv[2]
    url = 'https://api.github.com/user'
    auth = (username, access_token)
    response = requests.get(url, auth=auth)

    if response.status_code == 200:
        user_info = response.json()
        print(user_info['id'])
    else:
        print(None)
