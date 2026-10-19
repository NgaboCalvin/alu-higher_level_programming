# Python - if/else, loops, functions

Control flow in Python: `if`/`else`, loops, `break`/`continue`, `range`, and
function definitions with scope and return values.

## Requirements

- Python 3 (tested with python3 / 3.8.5 on Ubuntu 20.04 LTS)
- pycodestyle 2.7.*
- Every file starts with `#!/usr/bin/python3` (or `#!/usr/bin/env python3` for
  the `-main.py` test harnesses), ends with a newline, and is executable

## Tasks

| File | Description |
| --- | --- |
| `0-positive_or_negative.py` | Print whether a random number is positive, zero or negative |
| `1-last_digit.py` | Print the last digit of a random number and classify it |
| `2-print_alphabet.py` | Print the lowercase alphabet without a trailing newline |
| `3-print_alphabt.py` | Print the lowercase alphabet except `q` and `e` |
| `4-print_hexa.py` | Print 0 to 98 in decimal and hexadecimal |
| `5-print_comb2.py` | Print 00 to 99, comma-space separated |
| `6-print_comb3.py` | Print all ascending two-digit combinations of distinct digits |
| `7-islower.py` | `islower(c)` returns True for lowercase characters |
| `8-uppercase.py` | `uppercase(str)` prints its argument in uppercase |
| `9-print_last_digit.py` | `print_last_digit(number)` prints and returns the last digit |
| `10-add.py` | `add(a, b)` returns `a + b` |
| `11-pow.py` | `pow(a, b)` returns `a ** b` |
| `12-fizzbuzz.py` | `fizzbuzz()` prints 1 to 100 applying FizzBuzz rules |

## Constraint notes

- Tasks 2-6 allow at most one loop, one `print` call with string formatting,
  no imports, and no variables holding characters/numbers/strings.
- Tasks 7-12 forbid importing modules; `7-islower` and `8-uppercase` also
  forbid `str.upper()` / `str.isupper()`, so `ord()` is used instead.
- Negative last digits keep their sign in task 1 (`-626` prints `-6`), which is
  why `number % 10` alone is not enough in Python.

## Test harnesses

The `-main.py` files mirror the ones from the task description and use
`__import__` to load the module under test:

```console
$ ./7-main.py
a is lower
H is upper
A is upper
3 is upper
g is lower
```