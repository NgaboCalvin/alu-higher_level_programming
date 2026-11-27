#!/usr/bin/python3
"""Display a URL body, or an error code when the status is 400 or higher."""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
