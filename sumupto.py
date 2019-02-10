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

x= int (i*(i+1))/2
print (x)