#!/usr/bin/python3
"""7-error_code module"""
from sys import argv

import requests

if __name__ == "__main__":
    resp = requests.get(argv[1])

    if resp.status_code >= 400:
        print(f"Error code: {resp.status_code}")
    else:
        print(resp.text)
