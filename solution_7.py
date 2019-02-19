#python squareroot.py
#Write a program that takes a positive ﬂoating point number as input and outputs 
#an approximation of its square root.
#Clodagh Murphy 19 02 2019

#Use the import statement to import a specific function from the math module
# According to "The Coder’s Apprentice" by Peter Spronck 
# It is possible to rename a function that you import from a module, using the
#keyword as. This is helpful if using several modules that contain functions with
#similar names.
#I have included it to make my code easier to read for a beginner.
from math import sqrt as squareroot

# ask the user to input a floating-point number - that is a number with decimal
#use float() type casting to return the value between the parentheses as a floating-point number
#even if it was not input as one.
#i = float(input("Hello. Please input a positive whole number float i.e., a number with a decimal point. "))
i = float(input("Hello. Please input a positive whole number float i.e., a number with a decimal point. "))

print( "Thanks. ")

print ("The square root of", i, "is approx.{:.1f}.".format( squareroot(i)))
x=(squareroot( i ))
print ("The square root of", i, "is approx. {:.2f}." .format (x))

#In order to show an approximation of the result with just one number to the right
#of the decimal point use .format () command



