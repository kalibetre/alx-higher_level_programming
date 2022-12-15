#!/bin/bash
# A bash script sends a request and sets a header variable
curl -s -H "X-School-User-Id":98 "$1"
