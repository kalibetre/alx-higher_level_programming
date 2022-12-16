#!/usr/bin/python3
"""
fetch https://alx-intranet.hbtn.io/status display response
"""
from urllib import request

if __name__ == "__main__":
    with request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        r = response.read()
        print(
            "Body response:\n\t- type: {}\n\t- content:\
                {}\n\t- utf8 content: {}"
            .format(type(r), r, r.decode('utf-8')))
