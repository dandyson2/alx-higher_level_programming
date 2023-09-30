#!/usr/bin/python3
"""Python script that takes 2 arguments, repo name and owner name for the ...
"""

import sys
import requests


def get_recent_commits(repository_name, repository_owner):
    url = f"https://api.github.com/repos/{repository_owner}/\
    {repository_name}/commits"
    response = requests.get(url)
    commits = response.json()
    try:
        for i in range(10):
            sha = commits[i].get("sha")
            author_name = commits[i].get("commit").get("author").get("name")
            print(f"{sha}: {author_name}")
    except IndexError:
        pass


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./script.py <repository name> <repository owner>")
    else:
        repository_name = sys.argv[1]
        repository_owner = sys.argv[2]
        get_recent_commits(repository_name, repository_owner)
