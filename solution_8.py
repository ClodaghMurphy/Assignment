#Write a program that outputs today’s date and time in 
# the format "Monday,January 10th 2019 at 1:15pm”. 
#Clodagh Murphy 08 03 2019
#First import datetime module in order to access it's functionality
#import datetime
#Print the current date and time
#Use strftime function to indicate the particular format the date and time should take
#%A Weekday as locale’s full name
#%B Month as locale’s full name.
#%d Day of the month as a zero-padded decimal number.	
#%Y Year with century as a decimal number.
#%I:%M  Hour:Minute (12-hour clock) as a zero-padded decimal number.
#%p Locale’s equivalent of either AM or PM.
#print(datetime.datetime.now().strftime("%A, %B %d %Y at %I:%M %p"))
#Above command produces result in following format
#Sunday, March 10 2019 at 09:29 AM
#The solution requires English ordinal suffix for the day of the month i.e. 10th
#this is not a functionality of python
#I adapted a piece of code that provides a suffix by user gsteff from stackoverflow
#https://stackoverflow.com/questions/5891555/display-the-date-like-may-5th-using-pythons-strftime/5891658#5891658
#It uses the time module
# and The localtime() function which returns struct_time in local time.
import time
import datetime

day_endings = {
    1: 'st',
    2: 'nd',
    3: 'rd',
    21: 'st',
    22: 'nd',
    23: 'rd',
    31: 'st'}

def custom_strftime (format, t):
    return time.strftime(format, t).replace('{TH}', str(t[2]) + day_endings.get(t[2], 'th'))
#return time.strftime(format, t).replace('{TH}', str(t[2]) + day_endings.get(t[2], 'th'))
#print(datetime.datetime.now().strftime("%A, %B %d %Y at %I:%M %p"))
#print (custom_strftime("%A, %B {TH}, %Y", time.localtime()))
print (custom_strftime("%A, %B {TH} %Y at %I:%M %p", time.localtime()))
#print (custom_strftime("%A, %B {TH} %Y at %I:%M %p", datetime.datetime.now()))