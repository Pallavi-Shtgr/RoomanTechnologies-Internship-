"""Day 03"""

# Write a Python function is in set(my_set, item) that takes a set my set and a variable item. The function should return True if the item exists in the set, otherwise return False.

# Constraint

# The set will contain up to 10 elements.

def is_in_set(my_set,item):
    return item in my_set
test_set={1,2,3,4,5}
test_item=4
print(is_in_set(test_set,test_item))