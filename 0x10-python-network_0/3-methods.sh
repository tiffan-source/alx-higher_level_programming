#!/bin/bash
# script that takes in a URL and displays all HTTP methods the server will accept
curl -s --head "$1" | grep -i "allow" | cut -d" " -f2-