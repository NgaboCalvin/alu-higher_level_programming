# Python - Hello, World

First steps with Python (Holberton School higher level programming).

## Requirements

- Python 3 (tested with python3 / 3.8.5 on Ubuntu 20.04 LTS)
- pycodestyle 2.7.*
- Shell scripts must be exactly 2 lines: shebang + command

## Files

| File | Description |
| --- | --- |
| `0-run` | Shell script that runs the Python file in `$PYFILE` |
| `1-run_inline` | Shell script that runs the Python code in `$PYCODE` |
| `2-print.py` | Print a string with `print` |
| `3-print_number.py` | Print an integer followed by "Battery street" (f-string) |
| `4-print_float.py` | Print a float with a precision of 2 digits (f-string) |
| `5-print_string.py` | Print a string 3 times, then its first 9 characters |
| `6-concat.py` | Concatenate `str1` and `str2` to print "Welcome to Holberton School!" |
| `7-edges.py` | Slice the word: first 3 letters, last 2 letters, middle word |
| `8-concat_edges.py` | Concatenate variables to print "object-oriented programming with Python" |
| `9-easter_egg.py` | Print "The Zen of Python", by Tim Peters |

## Usage

```console
$ export PYFILE=main.py
$ ./0-run
$ export PYCODE='print(f"Best School: {88+10}")'
$ ./1-run_inline
$ ./2-print.py
$ ./3-print_number.py
...
```

## Style

All scripts start with `#!/usr/bin/python3` (or `#!/bin/bash`), end with a
newline, and are executable. Line counts are checked with `wc -l`:

- `0-run` and `1-run_inline`: 2 lines
- `3-print_number.py`: 3 lines
- `5-print_string.py`: 5 lines max
- `6-concat.py`, `8-concat_edges.py`: 5 lines
- `7-edges.py`: 8 lines
- `9-easter_egg.py`: 98 characters max (`wc -m`)