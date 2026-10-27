# Python - Data Structures: Lists, Tuples

Working with lists and tuples: indexing, modifying lists, copying, matrices,
and string manipulation.

## Requirements

- Python 3 (tested with python3 / 3.8.5 on Ubuntu 20.04 LTS)
- pycodestyle 2.7.*
- Every file starts with `#!/usr/bin/python3`, ends with a newline, and is
  executable

## Tasks

| File | Description |
| --- | --- |
| `0-print_list_integer.py` | Print every integer of a list, one per line |
| `1-element_at.py` | Return the element at index `idx`, or `None` if invalid |
| `2-replace_in_list.py` | Replace the element at `idx` in place |
| `3-print_reversed_list_integer.py` | Print every integer of a list in reverse order |
| `4-new_in_list.py` | Replace an element in a copy of the list |
| `5-no_c.py` | Remove all `c` and `C` characters from a string |
| `6-print_matrix_integer.py` | Print a matrix of integers |
| `7-add_tuple.py` | Add two tuples element-wise, returning a 2-tuple |
| `8-multiple_returns.py` | Return the length and first character of a string |
| `9-max_integer.py` | Return the biggest integer of a list |
| `10-divisible_by_2.py` | Return a list of booleans for multiples of 2 |
| `11-delete_at.py` | Delete the element at `idx` in place |
| `12-switch.py` | Swap the values of `a` and `b` in exactly 5 lines |

## Constraint notes

- No imports are used in any task.
- `str.format()` is used to print integers; integers are never cast with
  `str()`.
- `max()` is not used in `9-max_integer.py`; `pop()` is not used in
  `11-delete_at.py`; `str.replace()` is not used in `5-no_c.py`.
- `try`/`except` is not used where the task forbids it.
