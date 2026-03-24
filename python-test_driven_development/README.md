# 📂 python-test_driven_development

This project focuses on writing functions with strong input validation and documenting behavior through doctests and unit tests. It practices clean error messages, edge-case handling, and test-first thinking.

## Files

| File | Description |
|------|-------------|
| `0-add_integer.py` | Add two integers with strict type checks |
| `2-matrix_divided.py` | Divide all values of a matrix with validation |
| `3-say_my_name.py` | Print a full name with argument validation |
| `4-print_square.py` | Print a square made of `#` characters |
| `5-text_indentation.py` | Print text with indentation after punctuation |
| `6-max_integer.py` | Return the largest integer in a list |
| `tests/0-add_integer.txt` | Doctests for `0-add_integer.py` |
| `tests/2-matrix_divided.txt` | Doctests for `2-matrix_divided.py` |
| `tests/3-say_my_name.txt` | Doctests for `3-say_my_name.py` |
| `tests/4-print_square.txt` | Doctests for `4-print_square.py` |
| `tests/5-text_indentation.txt` | Doctests for `5-text_indentation.py` |
| `tests/6-max_integer_test.py` | Unit tests for `6-max_integer.py` |
| `exo_bonus/` | Bonus exercises with additional doctests |

## Running the tests

```bash
python3 -m doctest -v <module>.py
python3 -m unittest tests/6-max_integer_test.py
```
