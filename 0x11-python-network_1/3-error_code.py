#!/usr/bin/python3
"""3-error_code module"""
from sys import argv
from urllib import error, request

if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as e:
        print(f"Error code: {e.code}")
