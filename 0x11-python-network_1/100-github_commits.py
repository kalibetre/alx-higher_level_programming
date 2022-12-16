#!/usr/bin/python3
"""10-my_github module"""
from sys import argv

import requests

if __name__ == "__main__":
    github = f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits"
    resp = requests.get(github)

    for row in resp.json()[:10]:
        sha = row.get("sha")
        author = row.get("commit").get("author").get("name")
        print(f"{sha}: {author}")
