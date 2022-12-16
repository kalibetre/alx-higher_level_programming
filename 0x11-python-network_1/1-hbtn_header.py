#!/usr/bin/python3
"""1-hbtn_status module"""
import urllib.request
from sys import argv

if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as resp:
        print(resp.getheader("X-Request-Id"))
