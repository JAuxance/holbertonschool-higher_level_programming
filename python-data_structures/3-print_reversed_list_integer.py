#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    if my_list == 0:
        return None
    for k in my_list:
        print("{:d}".format(k))


my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)
