# Problem No 3
# --------------------------------------------------------------------------------
# Write a program that prints all numbers between 1,000 and 10,000 that are divisible
# by 6 but not 12.
# --------------------------------------------------------------------------------
#
# Author: Yvonne Brady
# Student ID: G00376355
#
# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------
# Trial 1 - expected to print all numbers between 1000 and 2000
# for l in range(1000,2000):
#       print(l)
# Worked fine
# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------
# Trial 2 - expected to print only those whose remainder when divided by 6 was 0
# for l in range(1000,2000):
#       When modulo 6 is zero is means that the number is divisible by 6
#    if l%6 == 0:
#        print(l)
# Worked fine
# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------
# Trial 3 - expected to print only those divisible by 6 but not 12
for l in range(1000,10000):
        # When modulo 12 is not zero is means that the number is not divisible by 12
    if l%6 == 0 and l%12 != 0:
        print(l)
# Worked fine
# --------------------------------------------------------------------------------

        
