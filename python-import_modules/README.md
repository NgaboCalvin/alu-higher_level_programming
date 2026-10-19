# Python - Import modules

Python module imports, `sys.argv` handling, and guarded execution with
`if __name__ == "__main__":`.

## Requirements

- Python 3 (tested with python3 / 3.8.5 on Ubuntu 20.04 LTS)
- pycodestyle 2.7.*
- Every file starts with `#!/usr/bin/python3`, ends with a newline, and is
  executable

## Tasks

| File | Description |
| --- | --- |
| `0-add.py` | Import `add` from `add_0.py` and print `1 + 2 = 3` |
| `1-calculation.py` | Import `add`/`sub`/`mul`/`div` and print all four results |
| `2-args.py` | Print the number of arguments and list them positionally |
| `3-infinite_add.py` | Print the sum of all arguments, supporting bignums |
| `4-hidden_discovery.py` | Print the public names defined in `hidden_4.pyc` |
| `5-variable_load.py` | Import `a` from `variable_load_5.py` and print it |

## Advanced tasks

| File | Description |
| --- | --- |
| `100-my_calculator.py` | Command-line calculator handling `+ - * /` |
| `101-easy_print.py` | Print `#pythoniscool` in at most 2 lines |
| `102-magic_calculation.py` | Reconstruct `magic_calculation` from bytecode |
| `103-fast_alphabet.py` | Print the uppercase alphabet in at most 3 lines |
| `magic_calculation_102.py` | Helper module supplying `add`/`sub` to task 102 |

## Provided files

These are given by the task and must not be modified:

- `add_0.py` — defines `add(a, b)`
- `calculator_1.py` — defines `add`, `sub`, `mul`, `div`
- `variable_load_5.py` — defines `a = 98`
- `hidden_4.pyc` — Python 3.8 byte-compiled module to introspect

## Constraint notes

- `add_0` and `calculator_1` may each appear only once, so the import must be
  explicit (`from x import y`) rather than `import x` plus attribute access.
- `*` imports and `__import__` are forbidden in the task files.
- Every script guards its code with `if __name__ == "__main__":` so that
  importing it produces no output. `0-import_add.py` demonstrates this:
  `python3 0-import_add.py` prints nothing.
- Task 2 uses `":"` when at least one argument is passed and `"."` when none
  are, and uses the singular `argument` for exactly one.
- Task 4 must run under Python 3.8.x because `hidden_4.pyc` is compiled with
  that version; a 3.9+ interpreter rejects the bytecode magic number.
- Task 3 uses `int()` and `sum()` rather than `eval()` so that arbitrarily
  large integers are handled correctly.

## Advanced constraint notes

- `100-my_calculator.py` exits with status 1 on a wrong argument count or an
  unknown operator, and 0 on success.
- `101-easy_print.py` may not use `print`, `eval`, `open` or `import sys`, so it
  writes straight to file descriptor 1 via `os.write`.
- `102-magic_calculation.py` matches the given bytecode: when `a < b` it returns
  `add(a, b)` accumulated over `range(4, 6)`, otherwise `sub(a, b)`.
- `103-fast_alphabet.py` avoids loops, conditionals, `str.join()`, string
  literals and system calls by using the `string.ascii_uppercase` constant.

## Usage

```console
$ ./0-add.py
1 + 2 = 3
$ ./1-calculation.py
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2
$ ./2-args.py
0 arguments.
$ ./2-args.py Hello Welcome
2 arguments:
1: Hello
2: Welcome
$ ./3-infinite_add.py 79 10 -40 -300 89
-162
$ ./4-hidden_discovery.py | sort
my_secret_santa
print_hidden
print_school
$ ./5-variable_load.py
98
```