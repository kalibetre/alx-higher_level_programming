#!/usr/bin/python3
"""0-hbtn_status module"""

import urllib.request


def fetch_hbtn():
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as r:
        html = r.read()
        print("Body response:")
        print(f"\t- type:{type(html)}")
        print(f"\t- content:{html}")
        print(f"\t- utf8 content:{html.decode('utf-8')}")


if __name__ == "__main__":
    fetch_hbtn()
