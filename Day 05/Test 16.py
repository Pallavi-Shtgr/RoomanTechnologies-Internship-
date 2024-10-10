"""Day 05 MODULES AND LIBRARIES """


# Write a Python function math_operations(num: int) -> dict that takes a user input  integer num and returns a dictionary containing:
# The square root of num.
# The sine of 90 degrees.
# The factorial of num.

import math

def math_operations(num: int) -> dict:
    result = {}
    result['square_root'] = math.sqrt(num)
    result['sine_90_degrees'] = math.sin(math.radians(90))
    result['factorial'] = math.factorial(num)
    
    return result

