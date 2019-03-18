#Write a program that asks the user to input a positive integer and tells the user 
# whether or not the number is a prime.
#Clodagh Murphy 2019 02 03

#According to https://www.thoughtco.com/how-to-determine-number-is-prime-2312518
#A prime number is a numeral that is greater than 1 
#and cannot be divided evenly by any other number except 1 and itself.


#firstly ask the user to input a positive integer i.e. a whole number.

x = int(input("Hello. Please input a positive whole number. "))
#Exclude numbers less than or equal to 1 from being input at the outset because 1 is not prime
#and negative numbers cannot be.
while x <= 1:
    print("Please choose a positive whole number that isn't 1 or 2! Please run the program again.")
    exit()
# Use the exit() method to stop the program running. 
# It is the most reliable, cross-platform way of stopping code execution

#Code adapted from https://www.programiz.com/python-programming/examples/prime-number
#I would rather write my own code but I grappled with how to prove concept of "prime"
#and therefore had to use somebody else's : (
# use if/else loop to check for factors of x by iteration
# the equation x % 1== 0 determines whether the number can be divided by any other number 
#in the range between 2 and itself.
#The break statement terminates the loop once all the numbers in the range have been
#exhausted to tell the user that the number is a prime i.e., it could only be
#divided by itself.
for i in range(2,x):
       if x % i == 0:
           print("That is not a prime.")
           break
else:
    print("That is a prime.")
       



