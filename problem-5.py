# Problem No 5
# --------------------------------------------------------------------------------
# Write a program that asks the user to input a positive integer and tells the user
# whether or not the number is a prime.
# --------------------------------------------------------------------------------
#
# Author: Yvonne Brady
# Student ID: G00376355
#
# --------------------------------------------------------------------------------
# This is similar the one in the Python Tutorial
# Re-use code from problem 1 again for user input
# --------------------------------------------------------------------------------

# looking for a user input
ans = input("Please enter a positive integer: ")

# Tries to convert to int type
try:
    i = int(ans)
    # Here I am checking to make sure it is a positive number
    # As per instructions, program only to work with positive integer
    if i > 0:
        # This bit does the calculation
        # Adapted from Section 4.4 in Python Tutorial
        if i > 2:
            for y in range(2,i):
                # Checks each number from 2 to the number selected
                # If any of the numbers checked result in no remainder
                # The number could not be prime.
                if not ( i % y ):
                    print (str(i) + " is NOT a prime number")
                    # Breaks so as to stop checking
                    break
                # If all the numbers have been checked - it must be prime
                if y == i - 1:
                    print (str(i) + " IS a prime number")
        else:
            # Because 1 and 2 are prime numbers too!
            print (str(i) + " IS a prime number")
    else:
        # If the number is 0 or negative the user is informed
        print("The number has to be positive!")

# If it was not able to convert to an int type - 
# ie a string / floating point number was inputted
except ValueError:
    print("You did not enter an integer!")