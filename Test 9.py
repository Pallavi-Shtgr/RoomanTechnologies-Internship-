"""Day 03"""

# Write a Python function calculate_area(length, width) that takes two inputs: two integers length and width, and returns the area of a rectangle.
# Constraint
# Both length and width will be positive integers between 1 and 1000.

def calculate_area(length,width):
    return length*width
area1= calculate_area(4,4)
area2=calculate_area(3,8)
print(area1,area2)
