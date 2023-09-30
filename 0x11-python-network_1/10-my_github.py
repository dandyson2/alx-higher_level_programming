#!/usr/bin/python3

"""
Python script that takes your GitHub credentials (username and password) ...
"""

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    auth = HTTPBasicAuth(username, password)
    response = requests.get("https://api.github.com/user", auth=auth)
    github_id = response.json().get("id")
    print(github_id)
