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
if now.day == 1  or now.day == 21 or now.day == 31:
    print (now.strftime("%A, %B %dst %Y at %I:%M%p"))
elif now.day == 2 or now.day == 22:
    print (now.strftime("%A, %B %dnd %Y at %I:%M%p"))
elif now.day == 3 or now.day == 23:
    print (now.strftime("%A, %B %drd %Y at %I:%M%p"))
else:     
    # Monday, January 10th 2019 at 1:15pm”.
    print (now.strftime("%A, %B %dth %Y at %I:%M%p"))

