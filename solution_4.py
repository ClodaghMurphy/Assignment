#4 collatz
#Write a program that asks the user to input any positive integer 
#and outputs the successive values of the following calculation. 
#At each step calculate the next value by taking the current value and,
#if it is even, divide it by two, but if it is odd, multiply it by three and add one. 
#Have the program end if the current value is one.
#Clodagh Murphy 2019 02 17

#The instructions provided above refers to the collatz conjecture, this is
#an unsolved mathematical problem at time of writing.
#No matter what number selected, the final result will always be one.
#This code can be used to test the theory and if you get a result other than one
#I'd be happy to take a cut of the $500 reward ; P

#while i != 1:
#if i%2 == 0: print(i//2)
#else: print(i*3+1)
#no need to write code for both i%2==0 and i%2==1 
#If one is true, the other is automatically false
#Boolean innit?

#13032019 as this code currently stands the loop isn't happening as desired.
#It just goes on an infinite loop, printing out the same numbers over and over.
#i need to make the loop a function as per week 6 programming video on moodle
#then feed the input into it as illustrated by user R2DPoop
#https://stackoverflow.com/questions/33324432/collatz-sequence-python-3

x = int(input("Hello. Please input a positive whole number. "))
#firstly ask the user to input a positive integer i.e. a whole number.
#Tell the user it must be a positive integer if it is not one

while x <= 0:
    print("I require a positive whole number. Please run the program again.")
    exit()
# Use the exit() method to stop the program running. 
# It is the most reliable, cross-platform way of stopping code execution

#collatz function verbatim from user R2DPoop
#https://stackoverflow.com/questions/33324432/collatz-sequence-python-3
def collatz(i):
    while i != 1:
#!= means not equal to, therefore when i is equal to 1 the following loop won't happen
        if i%2 == 0: 
            i = i // 2
#no need to write code for both conditions i%2==0 and i%2==1 
#If one is true, the other is automatically false
            print(i)
        else:
            i = i*3+1
            print(i)
#Finally, call the function. It will loop until the x=1 as set out in the while statement.
collatz (x)





