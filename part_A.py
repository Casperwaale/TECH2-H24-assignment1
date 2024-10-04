
# Importing the relevant packages
import math as mt
import numpy as np
""""
TECH2 mandatory assignment - Part A

Write the implementation of part A of the exercise below.
"""
# Method 1
def std_loops(numbers):
    """
    Compute standard deviation of x using loops.

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """
# Finding "mean" using variables "sum" and "i" 
    sum = 0 
    i = 0

    for num in numbers:
        sum = sum + num 
        i = i + 1

        mean = sum/i

# Finding "S" using the variables "sum_square" and "i"   
    sum_square = 0
    
    for num in numbers:
        sum_square = sum_square + num**2

    S = sum_square/i

# Computing the variance (remember to square "mean")
    variance = S - mean**2
# Computing standard deviation using square root function imported by math
    return mt.sqrt(variance)

    








# Method 2
def std_builtin(numbers):
    """
    Compute standard deviation of x using the built-in functions sum()
    and len().

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """
# Calculating mean and creating an empty list called "squares"
    mean = sum(numbers)/len(numbers)
    squares = []


# Appending num^2 to "squares", then find "S" using the sum og len of this list
    for num in numbers:
        squares.append(num**2)

    S = sum(squares) / len(squares)

# Computing the variance (remember to square mean, again)
    variance = S - mean**2

# Computing standard deviation again using same function in "Method 1"
    return mt.sqrt(variance)


# Method 3
# Defining a function to use the numpy functions
# Using Numpy function for standard deviation
# having the function stored in a variable 
def std_numpy(numbers):
    std = np.std(numbers)
    return std



