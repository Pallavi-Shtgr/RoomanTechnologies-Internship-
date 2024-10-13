"""Day 06 EXCEPTION HANDLING """

#  Write a Python function check_positive(number) that takes an integer number as input. 
# If the number is negative, raise a ValueError with the message "Negative numbers are not allowed!" and handle it by returning the message. Otherwise, return the number.

# Constraint
# The input number will be an integer between -100 and 100.

def check_positive(number):
    try:
        if number<0:
            raise ValueError("Negative numbers are not allowed")
        return number
    except ValueError as e:
        return str(e)