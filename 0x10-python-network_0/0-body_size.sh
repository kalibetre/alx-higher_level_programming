#!/bin/bash
# A bash script that sends a request to a URL and displays content length
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
