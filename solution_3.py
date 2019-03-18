#Write a program that prints all numbers between 1,000 and 10,000 
# that are divisible by 6 but not 12 
#Clodagh Murphy 2019 02 10

#I used the built-in range() function that generates arithmetic progressions.
#Remember not to include any punctuation such as a comma in the numbers over 1000
#because Python won't recognise it.
for i in range (1000, 10000):

#Use an if/and statement for i in the above mentioned range
#when it can be divided by 6 with no remainder
#and when being divided by 12 leaves a remainder
#!= is a handy standard comparison operator that means not equal to
#print the results
    if  (i % 6 == 0) and (i % 12 != 0):

        print (i)
       
# In order to test my result I started with a range (1000, 1100) and manually checked 
# every output, once this proved correct I expanded the parameters 

print ("are all the numbers between 1,000 and 10,000 that are divisible by 6 but not 12.")  
 
print("Have a nice day!")