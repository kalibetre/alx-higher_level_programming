#!/usr/bin/python3
"""0-hbtn_status module"""

import urllib.request
from sys import argv


def get_response_header():
    """displays the value of X-Request-Id
    """
    req = urllib.request.Request(argv[1])
    with urllib.request.urlopen(req) as resp:
        print(resp.getheader('X-Request-Id'))


if __name__ == "__main__":
    get_response_header()
