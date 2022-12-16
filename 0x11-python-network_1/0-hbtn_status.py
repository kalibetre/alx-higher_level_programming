#!/usr/bin/python3
"""0-hbtn_status module"""

if __name__ == "__main__":
    from urllib import request

    with request.urlopen("https://alx-intranet.hbtn.io/status") as r:
        html = r.read()
        print("Body response:")
        print(f"\t- type: {type(html)}")
        print(f"\t- content: {html}")
        print(f"\t- utf8 content: {html.decode('utf-8')}")
