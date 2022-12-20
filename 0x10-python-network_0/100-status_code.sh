#!/bin/bash
# Script that sends a request to a URL passed as an argument, and displays only the status code of the response
curl -L -s -w "%{http_code}" -o /dev/null "$1"
