#python daybeginst
#Write a program that outputs whether or not today is a day that begins with the letter T
#Clodagh Murphy 2019 02 10


import datetime


if datetime.datetime.today().weekday() == 2:
  print("Yes - today begins with a T.")
else:
  print("No - today does not begin with a T.")

if datetime.datetime.today().weekday() == 4:
  print("Yes - today begins with a T.")
else:
  print("No - today does not begin with a T.")