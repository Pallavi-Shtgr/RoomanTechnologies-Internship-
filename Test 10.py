"""Day 03"""

# Write a Python function add_to_list(my list, item) that takes a list my list and an item item. The function should append the item to the list and return the updated list.
# Constraint

# The list will have a maximum length of 10.
# The item can be any valid Python data type.

def is_in_set(my_set,item):
    return item in my_set
test_set={1,2,3,4,5}
test_item=4
print(is_in_set(test_set,test_item))