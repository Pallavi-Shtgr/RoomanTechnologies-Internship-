"""Day 02 CONTROL STRUCTURE"""

# Write a Python function categorize_temperature(temp) that takes a temperature (in Celsius) as input and returns:

# "Hot" if the temperature is above 30,
# "Warm" if the temperature is between 20 and 30 (inclusive).
# "Cool" if the temperature is between 10 and 19 (inclusive),
# "Cold" if the temperature is below 10.

def categorize_temperature(temp):
    if temp>30:
       return "Hot"
    elif 20<=temp<=30:
        return "Warm"
    elif 10<=temp<=19:
         return "Cool"
    else:
        return "Cold"

print(categorize_temperature(34))
print(categorize_temperature(26))
print(categorize_temperature(18))
print(categorize_temperature(3))