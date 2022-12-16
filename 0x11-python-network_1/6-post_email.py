#!/usr/bin/python3
"""6-post_email module"""
from sys import argv

import requests

if __name__ == "__main__":
    resp = requests.post(argv[1], data={"email": argv[2]})
    print(resp.text)
