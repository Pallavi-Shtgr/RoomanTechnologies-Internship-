"""Day 02"""

# Create a Python function grade(score) that takes a student's score (integer) as input and returns a grade as per the following rules:

# A: if score >= 90
# B: if score >= 80
# C: if score >= 70
# D: if score >= 60
# F: if score < 60




def grade(score):
    if not isinstance(score, int):
        raise TypeError("Score must be an integer")
    
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")
 
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

try:
    print(grade(95))  
    print(grade(85))  
    print(grade(75)) 
    print(grade(65)) 
    print(grade(55)) 
    print(grade(110))
except Exception as e:
    print(e)

try:
    print(grade(-5)) 
except Exception as e:
    print(e)

try:
    print(grade(90.5)) 
except Exception as e:
    print(e)
