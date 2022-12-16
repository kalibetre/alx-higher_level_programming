#!/usr/bin/python3
"""5-hbtn_header module"""
from sys import argv

import requests

if __name__ == "__main__":
    resp = requests.get(argv[1])
    print(resp.headers.get("X-Request-Id"))
