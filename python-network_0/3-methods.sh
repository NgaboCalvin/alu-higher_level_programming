#!/bin/bash
# Display the HTTP methods accepted by the server
curl -s -X OPTIONS -I "$1" | grep -i "^Allow:" | cut -d" " -f2- | tr -d "\r"
