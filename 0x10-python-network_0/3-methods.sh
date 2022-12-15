#!/bin/bash
# A bash script that sends a request to a URL and displays content length
curl -sI "$1" | grep -i Allow | cut -d ":" -f 2 | awk '{$1=$1};1'
