# Problem No 8
# --------------------------------------------------------------------------------
# Write a program that outputs today’s date and time in the format ”Monday, January
# 10th 2019 at 1:15pm”.
# --------------------------------------------------------------------------------
#
# Author: Yvonne Brady
# Student ID: G00376355
#
# --------------------------------------------------------------------------------
# Ref: https://www.saltycrane.com/blog/2008/06/how-to-get-current-date-and-time-in/
# %A	Locale's full weekday name.	
# %B	Locale's full month name.	
# %d	Day of the month as a decimal number [01,31].	
# %Y	Year with century as a decimal number.	
# %I	Hour (12-hour clock) as a decimal number [01,12].	
# %M	Minute as a decimal number [00,59].	
# %p	Locale's equivalent of either AM or PM.	(1)

# Required to perfrom any date / time functions
import datetime

# Record the current time
now = datetime.datetime.now()

# Need to change the ordinal indicator depending on whether the format requires st / nd / rd / th
# Also need to make the AM / PM lowercase
# If its the 1st / 21st or 31st use "st"
if (now.day%10) == 1 and not now.day == 11:
    print (now.strftime("%A, %B %dst %Y at %I:%M")+ now.strftime("%p").lower())
# If its the 2nd or 22nd use "nd"
elif (now.day%10) == 2 and not now.day == 12:
    print (now.strftime("%A, %B %dnd %Y at %I:%M")+ now.strftime("%p").lower())
# If it is the 3rd or 23rd use "rd"
elif (now.day%10) == 3 and not now.day == 13:
    print (now.strftime("%A, %B %drd %Y at %I:%M")+ now.strftime("%p").lower())
# Otherwise just use "th"
else:     
    # Monday, January 10th 2019 at 1:15pm”.
    print (now.strftime("%A, %B %dth %Y at %I:%M")+now.strftime("%p").lower())

