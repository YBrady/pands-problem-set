# Problem No 1
# --------------------------------------------------------------------------------
# Write a program that asks the user to input any positive integer and outputs the
# sum of all numbers between one and that number.
# --------------------------------------------------------------------------------
#
# Author: Yvonne Brady
# Student ID: G00376355
#
# --------------------------------------------------------------------------------

# looking for a user input
ans = input("Please enter a positive integer: ")

# Problem is that all inputs are classed as strings so we need to convert it to an int value
# Converting to an int type will only work if an integer value has been inputted in the first place
# Found a solution which I adapted on https://pynative.com/python-check-user-input-is-number-or-string/

# Tries to convert to int type - it goes down to the except logic if i does not convert to an integer OK
try:
    i = int(ans)
    # Here I am checking to make sure it is a positive number
    # As per instructions, program only to work with positive integer
    if i > 0:
        # Set the start value of the answer j
        j = i
        # This bit does the calculation
        while (i - 1) > 0:
            # It decrements the start number by 1 and adds it to the running total
            i -= 1
            j = j + i
        # Prints the answer as per instructions
        print(j)
        # Or just a little bit fancier using fstrings
        print(f"The sum of all numbers from 1 to {ans} is {j}.")
    else:
        # If the number is 0 or negative the user is informed
        print("The number has to be positive!")

#If it was not able to convert to an int type - ie a string / floating point number was inputted
except ValueError:
    print("You did not enter an integer!")