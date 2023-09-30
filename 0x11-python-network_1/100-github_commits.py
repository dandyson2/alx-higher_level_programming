#!/usr/bin/python3
"""
Python script that takes 2 arguments: repo name and owner name to solve ...
"""

import sys
import requests

if __name__ == "__main__":
    # Construct the GitHub API URL with repository owner and name
    repository_owner = sys.argv[2]
    repository_name = sys.argv[1]
    url = f"https://api.github.com/repos/{repository_owner}/\
    {repository_name}/commits"

    # Send a GET request to the GitHub API
    response = requests.get(url)
    commits = response.json()

    try:
        # Print the 10 most recent commits and their authors
        for i in range(10):
            sha = commits[i].get("sha")
            author_name = commits[i].get("commit").get("author").get("name")
            print(f"{sha}: {author_name}")
    except IndexError:
        # Handle the case where there are fewer than 10 commits
        pass
