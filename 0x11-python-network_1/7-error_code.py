#!/usr/bin/python3
"""
Python script that takes in a URL, 
sends a request to the URL and displays the body of the response
if the HTTP status code is greater than or equal to 400, 
print: Error code: followed by the value of the HTTP status code
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    body = requests.get(url)
    if body.status_code >= 400:
        print("Error code: {}".format(body.status_code))
    else:
        print(body.text)
