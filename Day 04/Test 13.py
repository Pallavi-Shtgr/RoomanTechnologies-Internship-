"""Day 04 DATA STRUCTURES"""

# • The current function overwrites the input parameter by redefining 'colors' as a set within the function. Remove this redefinition to use the input parameter.
# • The input parameter 'colors' should be treated as a tuple, not a set. Ensure you are accessing the tuple using index positions.
# • To return the second color, access the element at index 1 of the tuple.
# • Ensure that the function returns a string, which is the color at the specified index.
# • Test the function with provided test cases to verify the correct implementation.

def get_Second_color(colors):
    second_colors=colors[1]
    return second_colors