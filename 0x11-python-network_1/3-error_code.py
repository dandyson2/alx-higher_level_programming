#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays ...
"""
import sys
import urllib.error
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
