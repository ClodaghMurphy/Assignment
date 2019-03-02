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
# n(n+1)/2
#When I tested the program the result was always displayed with as a floating number
#In order to give a result of an integer with no decimal point
#DO ANOTHER LINE OR AMEND THIS CODE!!

x= int (i*(i+1))/2
print (x)
