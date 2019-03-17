#Write a program that reads in a text ﬁle and outputs every second line. 
#The program should take the ﬁlename from an argument on the command line.
#Clodagh Murphy 16032019

#from the python tutorial 
# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
#It is good practice to use the with keyword when dealing with file objects.
#with open('honeybees.txt','r+') as f:
#The first argument is a string containing the filename
#The second argument is another string containing a few characters describing 
#the way in which the file will be used. 
#r+ opens the file for both reading and writing


    # = list(f)
    #with open("database.txt") as database:
    #mylist = (line.rstrip("\n") for line in f)
    #print (mylist)
#import csv
with open('honeybees.txt', newline='') as f:
    mylist = list(f)
    mylist=strip('\r\n')
    #THIS WORKS print ((mylist[::2]))
    #for ("\r\n") in (mylist): print (" ")
    print ((mylist[::2]))
    
f.close()
#this code adapted from https://docs.python.org/3/library/csv.html    
#and it works except cannot print second lines only
#    thetext = csv.reader(f, delimiter=' ')
#    thetext = (thetext[::2])
#    for row in thetext:
#        print(' '.join(row))



#import csv
#with open('eggs.csv', newline='') as csvfile:
#    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#    for row in spamreader:
#            print(', '.join(row))


#You can read the file as a list of lines by simply calling list() on the file object 
# as advised by user Martijn Pieters
# https://stackoverflow.com/questions/
# 17569679/python-attributeerror-io-textiowrapper-object-has-no-attribute-split  
    #print (mylist[::2]) 
    #print (str.strip( '/n' ))
  

#use a for loop, treating the text file as if it was a list

#call f.close() to close the file and immediately free up any system resources used by it
#f.close()
#use an indent instead!!







