#!/usr/bin/python3
"""10-my_github module"""
from sys import argv

import requests

if __name__ == "__main__":
    github = "https://api.github.com/user"
    resp = requests.get(github, auth=(argv[1], argv[2]))
    print(resp.json().get("id"))
