"""Day 02 CONTROL STRUCTURE"""

# Write a Python function is prime_or_even_odd(n) that takes an integer n as input and performs the following:

# If n is a prime number, return True.

# If n is not a prime number, return "Even" if n is even, or "Odd" if n is odd.

def is_prime_or_even_odd(n):
    if n > 1:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                 break
        else:
              return True

  
    if n == 0 or n == 1:
        return None


    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"