#!/bin/bash
# A bash script that sends a POST request to a url and displays the body
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" -X POST "$1"
