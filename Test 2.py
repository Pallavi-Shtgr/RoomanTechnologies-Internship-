#  Write a Python function calculate_age(birth_year) that takes the birth year as input and returns the current age based on the current year 2023.

# Input
# The function takes an integer birth year as input.

# Output
# The function returns an integer representing the user's age.

def calculate_age(birth_year):
    current_year = 2023
    current_age = current_year - birth_year
    return current_age

birth_year = 2000  

print("The current age is:", calculate_age(birth_year))