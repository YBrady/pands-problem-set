# Problem No 7
# --------------------------------------------------------------------------------
# Write a program that takes a user input string and outputs every second word.
# --------------------------------------------------------------------------------
#
# Author: Yvonne Brady
# Student ID: G00376355
#
# --------------------------------------------------------------------------------
#
# https://www.geeksforgeeks.org/python-math-function-sqrt/

import math

# Re-use the code from Problem 1 re inputtng an integer except change to floating point:
# looking for a user input
ans = input("Please enter a positive number: ")

# Tries to convert to floating point type
try:
    i = float(ans)
    # Here I am checking to make sure it is a positive number
    # As you will get an error with a negative - no complex numbers here!

    if i > 0.0:
        # This bit does the calculation - changed for problem 7
        print("The square root of "+ str(i) + " is approx " + str(round(math.sqrt(i),1)) + ".")
        # --------------------------------------------------------------------------------
    else:
        # If the number is 0 or negative the user is informed
        print("The number has to be positive!")

# If it was not able to convert to an floating point type - 
# ie a string
except ValueError:
    print("You did not enter a number!")
