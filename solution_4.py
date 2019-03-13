#4 collatz
#Write a program that asks the user to input any positive integer 
#and outputs the successive values of the following calculation. 
#At each step calculate the next value by taking the current value and,
#if it is even, divide it by two, but if it is odd, multiply it by three and add one. 
#Have the program end if the current value is one.
#Clodagh Murphy 17 02 2019

#firstly ask the user to input a positive integer i.e. a whole number.

i = int(input("Hello. Please input a positive whole number. "))
# Tell the user it must be a positive integer if it is not one
input
while i <= 0:
    print("I require a positive whole number. Please run the program again.")
    exit()
# Use the exit() method to stop the program running. 
# It is the most reliable, cross-platform way of stopping code execution

#total = 0
#while i > 0
#    total = total + i


while i > 1:
    if i%2==0:
        i = (i//2)
    print (i)
    #elif i%2==1:
      #  i = (i*3+1)
print (i)
#else: 
    #print ("OK")

