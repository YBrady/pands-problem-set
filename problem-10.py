# Problem No 10
# --------------------------------------------------------------------------------
# Write a program that displays a plot of the functions x, x2 and 2x 
# in the range [0, 4].
# --------------------------------------------------------------------------------
#
# Author: Yvonne Brady
# Student ID: G00376355
#
# --------------------------------------------------------------------------------


# Import the matplotlib to draw the plots 
import matplotlib.pyplot as plt 

# Setting the x values 
x = range (4)

# Plot #1: f(x) = x
y1 = x
# Plot #2: f(x) = x^2
y2 = [x*x for x in range(4)]
# Plot #3: f(x) = 2^x
y3 = [2**x for x in range(4)]

# Plotting the points and the legend 
# Plot #1: f(x) = x
plt.plot(x, y1, label = "f(x): x")
# Plot #2: f(x) = x^2
plt.plot(x, y2, label = "f(x): x^2")
# Plot #3: f(x) = 2^x
plt.plot(x, y3, label = "f(x): 2^x") 

# Add a plot title
plt.title("Problem #10 of problem set")
# Name the x axis
plt.xlabel("x-axis")
# Name the y axis
plt.ylabel("y-axis")
# Position the legend
plt.legend(loc='upper left')

# Plot the graphs 
plt.show() 