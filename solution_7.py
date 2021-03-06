#Write a program that takes a positive ﬂoating point number as input and outputs 
#an approximation of its square root.
#Clodagh Murphy 2019 02 19

#Use the import statement to import a specific function from the math module
# According to "The Coder’s Apprentice" by Peter Spronck 
# It is possible to rename a function that you import from a module, using the
#keyword as. This is helpful if using several modules that contain functions with
#similar names.
#I have included it to make my code easier to read for a beginner.
from math import sqrt as squareroot

# ask the user to input a floating-point number - that is a number with decimal
#As all data stored from the input command is stored as a string variable
#Use the conversion process known as TypeCasting
#float() type casting will return the value between the parentheses as a floating-point number
#even though it was not input as one.

i = float(input("Hello. Please input a positive whole number float i.e., a number with a decimal point. "))

print( "Thanks. ")
#x=(squareroot( i ))
#print ("The square root of", i, "is approx. {:.2f}." .format (x))
#All the code can fit in one line like this
print ("The square root of", i, "is approximately {:.1f}.".format( squareroot(i)))


#In order to show an approximation of the result with just one number to the right
#of the decimal point use .format () command
#this format was indicated in the example provided in problem set documentation
#Use of .format method adapted from examples in Chapter 5 Simple Functions
#"The Coder’s Apprentice" by Peter Spronck




