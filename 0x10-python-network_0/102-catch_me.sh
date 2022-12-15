#!/bin/bash
# A bash script that sends a POST request to a url and displays the body
curl -sL -H "origin:HolbertonSchool" -d "user_id=98" -X PUT "0.0.0.0:5000/catch_me"
