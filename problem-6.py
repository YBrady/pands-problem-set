# Problem No 6
# --------------------------------------------------------------------------------
# Write a program that takes a user input string and outputs every second word.
# --------------------------------------------------------------------------------
#
# Author: Yvonne Brady
# Student ID: G00376355
#
# --------------------------------------------------------------------------------
#
# A whole lot of googling for this one!
# Most useful was = https://www.pythonforbeginners.com/dictionary/python-split


ans = input("Please enter a sentence: ")
# This splits the sentence into a list of the words
wordList = ans.split( )

#This prints the list skipping every other list item (/ word)
# print (wordList[::2])

#This prints the list items out with a space separator (no square brackets)
print (' '.join(wordList[::2])) 
