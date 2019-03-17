#Write a program that reads in a text ﬁle and outputs every second line. 
#The program should take the ﬁlename from an argument on the command line.
#Clodagh Murphy 16032019

#From the python tutorial 
#https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
#i adapted this code  with open('honeybees.txt','r+') as f:
#It is good practice to use the with keyword when dealing with file objects.
#The first argument is a string containing the filename
#The second argument is another string containing a few characters describing the way in which the file will be used i.e., r+ opens the file for both reading and writing
#mylist = list(f)
#As advised by user Martijn Pieters, the file can be read as a list of lines by simply calling list() on the file object
#https://stackoverflow.com/questions/17569679/python-attributeerror-io-textiowrapper-object-has-no-attribute-split  
#I used the [::2] slice syntax to return items from the array going up in increments of two.
#The output is printed with new line characters \r\n, that is not how i want the text to appear.
#I tried using thecsv module, even though it is a text file, csv reader can remove delimiters and 
# return file contents as a list of strings.
#this code adapted from https://docs.python.org/3/library/csv.html    
#and it works except cannot print second lines only
#import csv
#with open('honeybees.txt', newline='') as csvfile:
#    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#    for row in spamreader:
#            print(' '.join(row))

#The output is neat but I am unable to code correctly output only every second line.
#I tried various if and for statements which all returned varied Attribute, Name and syntax Errors.
#I am submitting the code that returns untidy output as it more accurately answers the problem.
with open('honeybees.txt', newline='') as f:
    mylist = list(f)
print ((mylist[::2]))
#above line uses an indent instead of f.close()









