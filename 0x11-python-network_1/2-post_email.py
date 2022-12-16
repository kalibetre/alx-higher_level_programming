#!/usr/bin/python3
"""2-post_email module"""
from sys import argv
from urllib import parse, request

if __name__ == "__main__":
    data = parse.urlencode({"email": argv[2]}).encode()
    with request.urlopen(argv[1], data) as response:
        print(response.read().decode('utf-8'))
