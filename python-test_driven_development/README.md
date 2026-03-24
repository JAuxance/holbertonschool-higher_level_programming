# python-test_driven_development

Python exercises focused on writing documented functions and validating them with doctests and unit tests.

## Files

| File | Description |
|------|-------------|
| `0-add_integer.py` | Add two integers or floats with type validation |
| `2-matrix_divided.py` | Divide every element of a matrix |
| `3-say_my_name.py` | Print a formatted full name |
| `4-print_square.py` | Print a square made of `#` |
| `5-text_indentation.py` | Print text with indentation rules |
| `6-max_integer.py` | Return the maximum integer in a list |

## Tests

The `tests/` directory contains doctest files for the modules and `6-max_integer_test.py` for unit tests.

The `exo_bonus/` directory contains extra exercises with their own doctests.

## Run

```bash
python3 -m doctest tests/0-add_integer.txt
python3 -m unittest tests.6-max_integer_test
```

## Topics

- input validation
- clear exceptions
- doctest documentation
- unit testing with `unittest`
