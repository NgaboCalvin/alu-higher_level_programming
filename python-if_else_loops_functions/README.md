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

## Advanced tasks

| File | Description |
| --- | --- |
| `100-print_tebahpla.py` | Print the alphabet reversed, alternating lower/upper case |
| `101-remove_char_at.py` | `remove_char_at(str, n)` copies the string minus the char at index `n` |
| `102-magic_calculation.py` | `magic_calculation(a, b, c)` reconstructed from bytecode |
| `101-main.py` | Test harness for task 101 |

## Constraint notes

- Tasks 2-6 allow at most one loop, one `print` call with string formatting,
  no imports, and no variables holding characters/numbers/strings.
- Tasks 7-12 forbid importing modules; `7-islower` and `8-uppercase` also
  forbid `str.upper()` / `str.isupper()`, so `ord()` is used instead.
- Negative last digits keep their sign in task 1 (`-626` prints `-6`), which is
  why `number % 10` alone is not enough in Python.

### Advanced constraint notes

- `100-print_tebahpla.py` uses one loop and one `print` with a string format, no
  imports, and no variable holding a character. Odd ASCII codes are shifted by
  32 to alternate `z Y x W ...`.
- `101-remove_char_at.py` treats `n` as a C array index, so out-of-range values
  such as `remove_char_at("School", 10)` or `("Python", -2)` simply copy the
  whole string instead of raising `IndexError`.
- `102-magic_calculation.py` mirrors the bytecode exactly: return `c` when
  `a < b`, else `a + b` when `c > b`, else `(a * b) - c`.

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