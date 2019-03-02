#Write a program that asks the user to input a positive integer and tells the user 
# whether or not the number is a prime.
#Clodagh Murphy 02 03 2019
#MORE WORK REQUIRED, THE IF/ELSE STATEMENT DOES NOT FIND IF A NUMBER
#IS PRIME OR NOT, IT IS MORE COMPLICATED, CHECK TO SEE IF THERE IS A PYTHON FUNCTION ALREADY DESIGNED

#firstly ask the user to input a positive integer i.e. a whole number.

i = int(input("Hello. Please input a positive whole number. "))
#Exclude the numbers 2 from being input because it is a prime number 
while i == 2:
    print("Please choose a positive whole number that isn't 2! Please run the program again.")
    exit()
# Use the exit() method to stop the program running. 
# It is the most reliable, cross-platform way of stopping code execution


 
if (i % 2 == 0):
    print("That is not a prime.")
else: 
  print("That is a prime")

#According to this website
#https://www.thoughtco.com/how-to-determine-number-is-prime-2312518
#A prime number is a numeral that is greater than 1 
#and cannot be divided evenly by any other number except 1 and itself.
#The input is unknown, so use an if statement to determine if i can be 
#divided by 2 evenly/without a remainder, if it can i is not a prime number.




