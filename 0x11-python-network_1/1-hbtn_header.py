#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and displays the value
"""
import sys
import urllib.request

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    request = urllib.request.Request(url)

    with urllib.request.urlopen(request) as response:
        headers = dict(response.headers)
        x_request_id = headers.get("X-Request-Id")
        print(x_request_id)
