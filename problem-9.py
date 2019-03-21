# Problem No 9
# --------------------------------------------------------------------------------
# Write a program that reads in a text file and outputs every second line. The program
# should take the filename from an argument on the command line.
# --------------------------------------------------------------------------------
#
# Author: Yvonne Brady
# Student ID: G00376355
#
# --------------------------------------------------------------------------------

# Need the sys module to read in the file name
import sys

# This part reads what was entered when the program was called 
# It is saved as a list in sys.argv

# If there are more or less than two arguments entered, show an error message
if  len(sys.argv) != 2:
    print("Please only supply a single filename.")
else:
    # Make sure what was inputted is actually a file name
    try:
        # The file name should be the second element of the sys.argv list
        # (The first item is calling the program ie "problem-9.py")
        txtFile = open(sys.argv[1])

        # Setting a variable to 0 to count so we can recognise every second line
        lines = 0

        # Loops through each line in the file        
        for line in txtFile:
            # Checks to see if it is every second line by checking the modulo 2 on the lines counter
            # As it starts at 0, the modulo will be 0 every second line beginning with the first line 
            if not(lines%2):
                # This prints the line. The end bit ensures there is no carriage return in the printout.
                print(line, end ="")
            # Updates the line counter
            lines += 1

    # If no such file was found
    except FileNotFoundError:
        # Error message
        print("Please enter a valid file!") 