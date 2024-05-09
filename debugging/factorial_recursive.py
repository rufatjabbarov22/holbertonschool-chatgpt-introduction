#!/usr/bin/python3

import sys

def factorial(n):
    """
    Calculates the factorial of a given number.

    Parameters:
    - n (int): The number for which factorial is to be calculated.

    Returns:
    - int: The factorial of the input number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get the number from command-line argument
f = factorial(int(sys.argv[1]))

# Print the factorial
print(f)
