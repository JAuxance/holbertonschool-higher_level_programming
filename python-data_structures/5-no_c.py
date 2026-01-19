#!/usr/bin/python3
def no_c(my_string):
    empty = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            empty += char
    return empty
