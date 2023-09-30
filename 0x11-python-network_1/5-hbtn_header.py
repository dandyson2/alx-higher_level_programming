#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays ...
"""

import sys
import requests

def get_x_request_id(url):
    response = requests.get(url)
    return response.headers.get("X-Request-Id")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./get_x_request_id.py <URL>")
    else:
        url = sys.argv[1]
        x_request_id = get_x_request_id(url)
        print(x_request_id)
