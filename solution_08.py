#Write a program that outputs today’s date and time in 
# the format "Monday,January 10th 2019 at 1:15pm”. 
#Clodagh Murphy 08 03 2019
#First import datetime module in order to access it's functionality
import datetime
#Print the current date and time
#Use strftime function to indicate the particular format the date and time should take
#%A Weekday as locale’s full name
#%B Month as locale’s full name.
#%d Day of the month as a zero-padded decimal number.	
#%Y Year with century as a decimal number.
#%I:%M  Hour:Minute (12-hour clock) as a zero-padded decimal number.
#%p Locale’s equivalent of either AM or PM.
print(datetime.datetime.now().strftime("%A, %B %d %Y at %I:%M %p"))


#CODE INCOMPLETE I NEED TO CREATE A FUNCTION WITH THE FOLLOWING BIT
#OF CODE TO SHOW THE DATE WITH A SUFFIX

#https://bytes.com/topic/python/answers/155606-time-formatting-date-suffixes
#if 4 <= day <= 20 or 24 <= day <= 30:
#suffix = "th"
#else:
#suffix = ["st", "nd", "rd"][day % 10 - 1]
