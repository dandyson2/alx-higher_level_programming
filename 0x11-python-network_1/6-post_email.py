#!/usr/bin/python3
"""
Python script that takes in a URL and an email address, sends a POST request,
"""
import sys
import requests


def main():
    if len(sys.argv) != 3:
        print("Usage: ./6-post_email.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]
    data = {"email": email}

    response = requests.post(url, data=data)
    print(response.text)


if __name__ == "__main__":
    main()
