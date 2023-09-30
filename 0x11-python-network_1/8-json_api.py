#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request ...
"""
import sys
import requests

if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    payload = {"q": letter}

    response = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        data = response.json()
        if not data:
            print("No result")
        else:
            print("[{}] {}".format(data.get("id"), data.get("name")))
    except ValueError:
        print("Not a valid JSON")
