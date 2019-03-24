#Write a program that displays a plot of the functions x, x2 and 2x in the range [0,4].
#Clodagh Murphy 17032019
#I watched  tutorials on Sentdex's channel to research how to plot a graph
#https://www.youtube.com/watch?v=aCULcv_IQYw


#Matplotlib is a Python 2D plotting library
#plt is the standard abbreviation for pyplot
import matplotlib.pyplot as plt
#code by Tacratis adapted from https://stackoverflow.com/questions/54662759/
# how-to-plot-the-function-y-x2-using-python-program-in-matlpotlib/54915958#54915958
# Create a variable which contains the integers in the designated range (0 to 4)
X = range(0,4)
#According to https://www.pythonforbeginners.com/basics/list-comprehensions-in-python
#List comprehensions provide a concise way to create lists. 
#It consists of brackets containing an expression followed by a for clause, then
#zero or more for or if clauses. The expressions can be anything, meaning you can
#put in all kinds of objects in lists.
#The result will be a new list resulting from evaluating the expression in the
#context of the for and if clauses which follow it. The list comprehension always returns a result list. 

# Using list comprehension return a list for each integer in X (0 to 4) for the following
#conditions
# a = return the value of the integer x = a 
# b = return the value of the integer to the power of 2 
# c = return the value of the integer multiplied by 2 

a = [x for x in X]
b = [x**2 for x in X]
c = [x*2 for x in X]

plt.xlabel ('this is the X axis. Range [0,4]')
plt.ylabel ('This is the Y axis')
plt.title ('GRAPH SHOWING PLOT OF FUNCTIONS x, x2 AND 2x IN THE RANGE [0,4]')
# Create three plot object using the list of integers for each function
#plt.plot(X,a)
#plt.plot(X,b)
#plt.plot(X,c)
#I want to customise the graph some more with a legend to make the plots meaningful
#Include keyword argument label
plt.plot(X,a, label='x')
plt.plot(X,b, label = 'x2')
plt.plot(X,c, label = '2x')
#invoke legend to display that
plt.legend()

# Render the plot, it won't appear unless this command is included!
plt.show()


