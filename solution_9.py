#Write a program that reads in a text ﬁle and outputs every second line. 
#The program should take the ﬁlename from an argument on the command line.
#Clodagh Murphy 16032019

#from the python tutorial 
# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
#It is good practice to use the with keyword when dealing with file objects.
with open('honeybees.txt','r+') as f:
#The first argument is a string containing the filename
#The second argument is another string containing a few characters describing 
#the way in which the file will be used. 
#r+ opens the file for both reading and writing


    mylist = list(f)
#
#You can read the file as a list of lines by simply calling list() on the file object 
# as advised by user Martijn Pieters
# https://stackoverflow.com/questions/
# 17569679/python-attributeerror-io-textiowrapper-object-has-no-attribute-split  
    print (mylist[::2]) 
#YUSS. THIS COMMAND OUTPUTS EVERY SECOND LINE    
#I NEED TO FORMAT THE RESULT CORRECTLY AND THEN IT WILL BE COMPLETE I THINK
   



#call f.close() to close the file and immediately free up any system resources used by it
f.close()
#use an indent instead!!



