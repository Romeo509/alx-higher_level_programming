#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status
using urllib
"""


import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    body = response.read()
    utf8_content = body.decode('utf-8')

print("Body response:")
print(f"\t- type: {type(body)}")
print(f"\t- content: {body}")
print(f"\t- utf8 content: {utf8_content}")
