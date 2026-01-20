#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for k in my_list:
        if k == my_list[-1]:
            print("{:d}".format(k), end="")
        else:
            print("{:d}".format(k), end="\n")
