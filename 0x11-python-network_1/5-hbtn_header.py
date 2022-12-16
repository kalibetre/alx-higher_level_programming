#!/usr/bin/python3
"""5-hbtn_header module"""
import requests

if __name__ == "__main__":
    resp = requests.get("https://alx-intranet.hbtn.io/status")
    print(resp.headers.get("X-Request-Id"))
