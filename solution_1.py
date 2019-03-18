#python sumupto
#Write a program that asks the user to input any positive integer 
#and outputs the sum of all numbers between one and that number. 
#Clodagh Murphy 2019 01 29

#firstly ask the user to input a positive integer i.e. a whole number.

i = int(input("Hello. Please input a positive whole number. "))

# Tell the user it must be a positive integer if it is not one

input
while i <= 0:
    print("I require a positive whole number. Please run the program again.")

# Use the exit() method to stop the program running. 
# It is the most reliable, cross-platform way of stopping code execution

    exit()


# Use the Gauss technique to get the answer
#https://betterexplained.com/articles/techniques-for-adding-the-numbers-1-to-100/
# n(n+1)/2
#x= int (i*(i+1))/2
#print (x)
#When I tested the program the result was always displayed with as a floating number
#In order to give a result of an integer with no decimal point use .format () command
#It will return a new string, which is a formatted version of thes tring for which 
# it is called
#To interpret an integer as a ﬂoat, place an "f" to the right side of the colon.
#indicate zero decimals using .0, which will display ﬂoats as integers

#Use of .format method adapted from examples in Chapter 5 Simple Functions
#"The Coder’s Apprentice" by Peter Spronck

x= int (i*(i+1))/2
print ("The sum of all numbers between one and your number is {:.0f}".format(x))
