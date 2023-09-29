#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status."""
import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    # Create a request object
    request = urllib.request.Request(url)

    # Send the request and handle the response
    with urllib.request.urlopen(request) as response:
        body = response.read().decode("utf-8")

        # Print information about the response
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
