# Problem No 7
# --------------------------------------------------------------------------------
# Write a program that that takes a positive floating point number as input and outputs
# an approximation of its square root.
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
        # This bit does the calculation - for comparison I have included the sqrt function answer
        # I also have printed the answer before the Babylonian calculation to see if there is a discernable time delay
        print(f"The python square root of {i} is approx " + str(round(math.sqrt(i),1)) + ".")

        # ------------------------------------------------------------------------------------------------------
        # Used the Babylonian method of finding a square root 
        # https://en.wikipedia.org/wiki/Methods_of_computing_square_roots 
        # Where two guesses converge on the answer
        # Note - I found this method useful for calculating square roots for values >= 1. 
        # It doesn't work so well with values less than one regardless of what I set the LoGuess to be

        # This is the starting point. 
        # The algorithm could be improved if the HiGuess was closer to the square root value at the start
        # But using the i value means the 0 and 1 inputs of i are catered for
        HiGuess = i 
        LoGuess = 0.1 

        # Repeat until the two guesses are sufficiently close
        while HiGuess - LoGuess > 0.1: 
            # Get the mid point between the high and low guesses
            HiGuess = (HiGuess + LoGuess)/2
            # Re-approximate the LoGuess according to Babylonian method
            LoGuess = i / HiGuess 

        # Wanted to a single decimal place. 
        # Chose HiGuess as this would cater for the scenario where 1 is originally inputted
        HiGuess = round(HiGuess, 1)

        print(f"The Babylonian square root of {i} is approx {HiGuess}.")
        # --------------------------------------------------------------------------------
        # This is the Newtonian method as described in week 8 video - added to see if it handled values
        # less than 1 any better, but it really isn't that much better than the Babylonian one above!
        estimate = i/2

        while abs((estimate * estimate) - i) > 0.1:
	        estimate -= ((estimate * estimate) - i)/(2 * estimate)
        estimate = round(estimate,1)
        print (f"The Newtonian square root of {i} is approx. {estimate}.") 
        #----------------------------------------------------------------------------------
    else:
        # If the number is 0 or negative the user is informed
        print("The number has to be positive!")

# If it was not able to convert to an floating point type - 
# ie a string
except ValueError:
    print("You did not enter a number!")
