#4 collatz
#Write a program that asks the user to input any positive integer 
#and outputs the successive values of the following calculation. 
#At each step calculate the next value bytakingthecurrentvalueand,
#ifitiseven,divideitbytwo,butifitisodd,multiply it by three and add one. 
#Have the program end if the current value is one.
#Clodagh Murphy 17 02 2019

#firstly ask the user to input a positive integer i.e. a whole number.

i = int(input("Hello. Please input a positive whole number. "))
# Tell the user it must be a positive integer if it is not one
input
while i <= 0:
    print("I require a positive whole number. Please run the program again.")
# Use the exit() method to stop the program running. 
# It is the most reliable, cross-platform way of stopping code execution
    exit()
