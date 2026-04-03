def copy_list(a_list):
    copy_list = []
    for item in a_list:
        copy_list.append(item)
    return copy_list

my_list = [1, 2, 3]
print(my_list)

new_list = copy_list(my_list)

print(my_list)
print(new_list)

print(new_list == my_list)
print(new_list is my_list)
