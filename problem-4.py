# Problem No 4
# --------------------------------------------------------------------------------
# Write a program that asks the user to input any positive integer and outputs the
# successive values of the following calculation. At each step calculate the next value
# by taking the current value and, if it is even, divide it by two, but if it is odd, multiply
# it by three and add one. Have the program end if the current value is one.
# --------------------------------------------------------------------------------
#
# Author: Yvonne Brady
# Student ID: G00376355
#
# --------------------------------------------------------------------------------

# Re-use the code from Problem 1 re inputtng an integer:
# looking for a user input
ans = input("Please enter a positive integer: ")

# Tries to convert to int type
try:
    i = int(ans)
    # Here I am checking to make sure it is a positive number
    # As per instructions, program only to work with positive integer
    if i > 0:

        # ------------------------------------------------------------------------
        # Trial 1 - Direct print:
        #   print (i) repeatedly -prints all values on separate lines 
        # Trial 2 - List: 
        #   creating and appending it into a list printed it all on one line, 
        #   but in square brackets
        # Trial 3 - concatenating string:
        #   concatenating a string returns a value exactly as required.
        # ------------------------------------------------------------------------

        # This bit does the calculation - changed for problem 4
        l = str(i)
        while i != 1:
            # Print the start value
            if not(i%2):
                # If it is even  divide by 2
                i = int(i / 2)
            else:
                # If it is odd multiply by 3 and add 1
                i = (i * 3) + 1
            # Concatenates the string to add the latest calculation result
            l = l + " " + str(i)
        print(l)
# --------------------------------------------------------------------------------

    else:
        # If the number is 0 or negative the user is informed
        print("The number has to be positive!")

# If it was not able to convert to an int type - 
# ie a string / floating point number was inputted
except ValueError:
    print("You did not enter an integer!")