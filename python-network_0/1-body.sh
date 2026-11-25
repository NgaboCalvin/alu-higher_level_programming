#!/bin/bash
# Display the body only when the response status is 200
code=$(curl -s -o /tmp/body -w "%{http_code}" "$1"); [ "$code" = "200" ] && cat /tmp/body
