#!/bin/bash
# Send a GET request with the required custom header
curl -s --header "X-HolbertonSchool-User-Id: 98" "$1"
