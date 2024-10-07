"""Day 04 DATA STRUCTURES"""

# Write a Python function update_sports(sports) that takes a set of sports, adds "cricket" to it, removes "tennis", and returns the updated set.
# Constraint
# The set will have a maximum of 5 sports.


def update_sports(sports):
    sports.add("cricket")
    sports.discard("tennis")
    return sports