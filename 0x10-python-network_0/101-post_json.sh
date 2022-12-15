#!/bin/bash
# A bash script that sends a POST request to a url and displays the body
curl -s -H "Content-Type: application/json" -d @"$2" -X POST "$1"
