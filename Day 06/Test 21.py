"""Day 06 EXCEPTION HANDLING """

# Write a Python function divide_numbers(num1, num2) that takes two numbers as input and returns their division. 
# If the second number is zero, raise a ZeroDivisionError and handle it by returning the message "Error: Division by zero is not allowed."
# Constraint
# num1 and num2 are integers between -100 and 100.
# You must handle the ZeroDivisionError explicitly.

def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        # Handle division by zero by returning an error message
        return "Error: Division by zero is not allowed."