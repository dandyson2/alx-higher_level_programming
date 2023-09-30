#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays ...
"""

import sys
import requests


def send_request_and_display_response(url):
    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./7-error_code.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    send_request_and_display_response(url)
