#!/usr/bin/python3
"""8-json_api module"""
from sys import argv

import requests

if __name__ == "__main__":
    data = {"q": argv[1] if len(argv) > 1 else ""}
    resp = requests.post("http://0.0.0.0:5000/search_user", data=data)

    try:
        js_data = resp.json()

        if js_data:
            id = js_data.get("id")
            name = js_data.get("name")
            print(f"[{id}] {name}")
        else:
            print("No result")
    except Exception as e:
        print("Not a valid JSON")
