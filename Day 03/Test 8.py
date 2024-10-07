"""Day 03 FUNCTIONS"""

# Write a Python function greet people(person dict) that takes a dictionary as input where each key is a string (the person's name) and each value is an integer (the person's age). 
#  function should print a message for each name and age in the dictionary in the format: Hello, (name)! You are (age) years old.

# Constraint

# The input dictionary will contain between 1 and 10 entries.
#  Each key (name) will be a string of length 1 to 50. Each value (age) will be an integer between 1 and 100.

def greet_people(person_dict):
    for name, age in person_dict.items():
        print(f"Hello {name}! You are {age} years old")

people = {'Pallavi': 25, 'John': 30, 'Alice': 28}
greet_people(people)
