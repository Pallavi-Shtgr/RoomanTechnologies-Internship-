"""Day 04 DATA STRUCTURES"""

# Write a Python function get_capital(capitals, country) that takes a dictionary capitals and a string country, and returns the capital of that country.

# Constraint
# The dictionary will contain up to 5 country-capital pairs.
# The country input will be a string with a length between 1 and 30.

def get_capital(country,capitals):

    if country in capitals:
        return capitals[country]
    else:
        return "Capital not found"
