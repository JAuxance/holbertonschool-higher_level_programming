#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for k in my_list:
        if k == my_list[-1]:
            print("{:d}".format(k), end="")
        else:
            print("{:d}".format(k), end="\n")


my_list = [1, 2, 3, 4, 43, 232, 333]
print_list_integer(my_list)