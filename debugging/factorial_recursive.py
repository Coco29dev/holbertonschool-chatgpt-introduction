#!/usr/bin/python3
import sys

# Function Description:
# This function calculates the factorial of a non-negative integer n recursively.
# Factorial of a number n (denoted as n!) is the product of all positive integers
# less than or equal to n. Specifically, n! = n * (n-1) * (n-2) * ... * 1. 
# The base case is when n equals 0, in which case the factorial is 1.

# Parameters:
# n (int): A non-negative integer for which the factorial is to be calculated.

# Returns:
# int: The factorial of the integer n. If n is 0, the function returns 1.
def factorial(n):
    if n == 0:  # Base case: factorial of 0 is 1
        return 1
    else:  # Recursive case: n * factorial of (n-1)
        return n * factorial(n-1)

# Taking input from command-line argument, converting it to an integer, and calculating the factorial
f = factorial(int(sys.argv[1]))  # Calls the factorial function with the input argument

# Output the result
print(f)