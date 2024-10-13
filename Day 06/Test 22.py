"""Day 06 EXCEPTION HANDLING """

# Write a Python function get_valid_number() that prompts the user to input a number and returns the integer value. 
# If the user provides a non-integer input, raise a ValueError and handle it by returning the message "Error: That's not a valid number."

# Constraint
# The input should be a string that can be converted to an integer.
# You must handle the ValueError explicitly.


def get_valid_number():
    try:
        user_input=input("Enter a number")
        number=int(user_input)
        return number
    except ValueError:
       return "Error: That's not a valid error"