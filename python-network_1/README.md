# Python - Network #1

Python scripts that fetch internet resources with `urllib` and `requests`.

## Files

- `0-hbtn_status.py` — fetch the ALU intranet status with `urllib`.
- `1-hbtn_header.py` — print the `X-Request-Id` header with `urllib`.
- `2-post_email.py` — POST an email parameter with `urllib`.
- `3-error_code.py` — print a body or handle `HTTPError` with `urllib`.
- `4-hbtn_status.py` — fetch the ALU intranet status with `requests`.
- `5-hbtn_header.py` — print the `X-Request-Id` header with `requests`.
- `6-post_email.py` — POST an email parameter with `requests`.
- `7-error_code.py` — print a body or an error code with `requests`.
- `8-json_api.py` — search a user through the local JSON API.
- `10-my_github.py` — print a GitHub user id with Basic Authentication.

## Usage

```bash
./0-hbtn_status.py
./1-hbtn_header.py https://intranet.hbtn.io
./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
./3-error_code.py http://0.0.0.0:5000/status_401
./4-hbtn_status.py
./5-hbtn_header.py https://intranet.hbtn.io
./6-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
./7-error_code.py http://0.0.0.0:5000/status_404
./8-json_api.py a
./10-my_github.py <username> <personal_access_token>
```
