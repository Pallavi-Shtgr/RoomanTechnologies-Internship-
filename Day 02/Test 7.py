"""Day 02 CONTROL STRUCTURE"""

# Write a Python function multiplication table(number) that takes a number as input and prints its multiplication table from 1 to 10.
# Constraint
# The input will be an integer between 1 and 20

def multiplication_table(number):
    for i in range(1,11):
        result=number*i
        print(f"{number} * {i} = {result}")

print(multiplication_table(8))
