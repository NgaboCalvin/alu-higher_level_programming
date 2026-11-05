# Python - Exceptions

Handling errors with `try` / `except` / `finally`, printing safely, and
raising builtin exceptions.

## Requirements

- Python 3 (tested with python3 / 3.8.5 on Ubuntu 20.04 LTS)
- pycodestyle 2.7.*
- Every file starts with `#!/usr/bin/python3`, ends with a newline, and is
  executable

## Tasks

| File | Description |
| --- | --- |
| `0-safe_print_list.py` | Print `x` elements of a list safely, return real count |
| `1-safe_print_integer.py` | Print a value as integer with `"{:d}".format()` |
| `2-safe_print_list_integers.py` | Print only the integers of the first `x` elements |
| `3-safe_print_division.py` | Divide 2 integers, print result in `finally:` |
| `4-list_division.py` | Divide 2 lists element by element, handling all errors |
| `5-raise_exception.py` | Raise a `TypeError` |
| `6-raise_exception_msg.py` | Raise a `NameError` with a message |

## Constraint notes

- No imports are used in any task.
- `len()` and `type()` are not used in tasks `0` and `2`.
- `2-safe_print_list_integers.py` lets `IndexError` propagate when `x` is
  bigger than the list length, while skipping non-integer values silently.
- `3-safe_print_division.py` and `4-list_division.py` use
  `try:` / `except:` / `finally:`.
