import math

def calculate_factorial(n):
   
    if n < 0:
        return "Factorial is not defined for negative numbers."
    try:
        return math.factorial(n)
    except TypeError:
        return "Input must be an integer."

def calculate_compound_interest(principal, rate, time_years):
  
    if principal < 0 or rate < 0 or time_years < 0:
        return "Principal, rate, and time must be non-negative."
    try:
        amount = principal * (1 + rate / 100)**time_years
        return amount - principal
    except TypeError:
        return "Invalid input types for calculation."


