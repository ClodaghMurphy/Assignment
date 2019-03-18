#python daybeginst solution 2
#Write a program that outputs whether or not today is a day that begins with the letter T
#Clodagh Murphy 2019 02 10

#Use the import statement to gain access to datetime Python code from another module
#The datetime module allows for manipulation of dates and times.
import datetime

#Assign the day of the week to x
x = (datetime.datetime.today().weekday())
#Returns the day of the week as an integer, where Monday is 0 and Sunday is 6.
#Therefore Tuesday is 1 and Thursday is 3
#if else statment modified from https://www.w3schools.com/python/python_conditions.asp

if x == 1: 
  print("Yes - today begins with a T.")  
elif x == 3: 
  print("Yes - today begins with a T.") 
# "else" is an optional statement that executes 
# when the conditional expression in the if statement above supplies a FALSE value
else: 
  print ("No - today does not begin with a T") 
