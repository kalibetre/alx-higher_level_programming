#!/usr/bin/python3
"""0-hbtn_status module"""

import urllib.request


def fetch_hbtn():
    """fetches the hbtn intranet and displays information
    """
    req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(req) as resp:
        html = resp.read()
        print("Body response:")
        print(f"\t- type: {type(html)}")
        print(f"\t- content: {html}")
        print(f"\t- utf8 content: {html.decode('utf-8')}")


if __name__ == "__main__":
    fetch_hbtn()
