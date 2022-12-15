#!/bin/bash
# A bash script that sends a request to a URL and displays content length
curl -sLI "$1" -o /dev/null -w '%{http_code}'
