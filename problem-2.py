# Problem No 2
# --------------------------------------------------------------------------------
# Write a program that outputs whether or not today is a day that begins with the
# letter T.
# --------------------------------------------------------------------------------
#
# Author: Yvonne Brady
# Student ID: G00376355
#
# --------------------------------------------------------------------------------

# Needed when dealing with date / time like in the first tuesday.py program
import datetime

# First part of the problem was getting today's day name
# I found this which showed me 
# https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date-in-python

# And tested it like this:
# now = datetime.datetime.now()
# print(now.strftime("%A"))

# strftime converts the date to a string so we could check the first letter
# %A retuns the day name

# Getting the first character of a string is simply string[0]
if datetime.datetime.now().strftime("%A")[0] == "T":
    print("Yes - today begins with a T")
else:
    print("No - today does not begin with a T")
