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

while i <= 0:
    print("I require a positive whole number. Please run the program again.")
    exit()
# Use the exit() method to stop the program running. 
# It is the most reliable, cross-platform way of stopping code execution

while i != 1:
#!= means not equal to, therefore when i is equal to 1 the following loop won't happen
    if i%2 == 0: print(i//2)
#no need to write code for both i%2==0 and i%2==1 
#If one is true, the other is automatically false
# Boolean innit?
    else:
        print(i*3+1)

#13032019 as this code currently stands the loop isn't happening as desired.
#i need to make the loop a function as per week 6 programming video
#then feed the input into it
#as illustrated by user R2DPoop
#https://stackoverflow.com/questions/33324432/collatz-sequence-python-3