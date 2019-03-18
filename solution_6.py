#Write a program that takes a user input string and outputs every second word.
#Clodagh Murphy 2019 03 16

#Preparation work using exercises from How to Think Like a Computer Scientist by Allen Downey

#t = ['a', 'b', 'c']
#x = t.pop(1)
#print (t)
#print (x)

#pop modifies the list and returns the element that was removed. If you don’t provide an
#index, it deletes and returns the last element.

#t = ['i', 'would', 'like', 'to', 'go', 'for', 'a', 'walk']
#x = t.pop(1,3,5,7)
#print (t)
#print (x)
#result TypeError: pop() takes at most 1 argument (4 given)

#t = ['i', 'would', 'like', 'to', 'go', 'for', 'a', 'walk']
#del t[1:5]
#print (t)

#s = 'pining for the fjords'
#t = s.split()
#print (t)

#fruitlist = ["apple", "banana", "cherry", "durian", "orange"]
#print( fruitlist ) 
#fruitlist[1:3] = [] 
#print( fruitlist )

#You can delete elements from a list 
#by assigning an empty list to a slice[].
#s = (input("Hello. Please input a short sentence of 10 words or less. "))
#t = s.split()
#t[0] = [] 
#t[2] = [] 
#t[4] = [] 
#t[6] = [] 
#t[8] = [] 

#print (t)
#This code kinda works but returns IndexError: list assignment index out of range
# if the input is less than the #number of elements in the code, if there isn't an eighth
#element for example, needs to be more conditonal
#Also the output is 'ugly'

#s = (input("Hello. Please input a sentence of 11 words. ")) 
#fruitlist = s.split()
#del is a keyword that allows you to delete a list element, or list slice, by index.
#every time an element is deleted, the code runs again and the element's location on the list
#changes
#Again this is code only works on a list with 11 words and output is ugly
#not much use!
#del fruitlist[0] 
#del fruitlist[1] 
#del fruitlist[2] 
#del fruitlist[3] 
#del fruitlist[4] 
#del fruitlist[5]

#print( fruitlist )
#print (word[2])       #get one char of the word
#print (word[0:1]   )     #get one char of the word (same as above)
#print (word[0:3] )       #get the first three char
#print (word[:3]  )       #get the first three char
#print (word[-3:]  )      #get the last three char
#print (word[3:]  )       #get all but the three first char
#print (word[:-3]  )      #get all but the three last character
#I can't work out how to get words rather than letters to print.

#phrase = input("Enter a phrase: ")
#words = phrase.split()  # ['I', 'need', 'practice']
#for word in words:
#  print(word)

#phrase=input('enter a phrase: ')
#for char in phrase:
 #   print (char, end ='')
    #words = phrase.replace(' ', '\n')
#print(words)
# NEXT THING TO DO IS str.join
#s = "Humpty;Dumpty;sat;on;the;wall" 
#wordlist = s.split( '; ' ) 
#s = " ".join( wordlist ) 
#print( s )
#s = words
#wordlist = s.split( ' ' ) 
#s = " ".join( wordlist ) 
#print( s )


#csv = "2016,September,28,Data Processing,Tilburg University" 
#values = csv.split( ', ' ) 
#for value in values: print( value )
#csv = (words[::2]) 
#values = csv.split( ', ' ) 
#for value in values: print( value )

#print( s.replace( 'sat on ', 'fell off ' ) )
#print( words.replace(',', '' )
#In [4]: print(*l, sep='\n')
#print ((words[::2]), sep='\n')
#gun
#pizza
# https://www.reddit.com/r/learnpython/comments/6b96j3/beginner_how_to_remove_square_bracket_and/

#Solution adapted from contribution by user Merig
#https://stackoverflow.com/questions/54857129/
#write-a-program-that-takes-a-user-input-string-and-outputs-every-second-word/54857192#54857192
words = input("Enter a phrase: ")
#All data from the input command is stored as a string variable.
#Use the split method to break a string into words
words = words.split()
#the [::2] slice syntax will return items from the array going up by two
print (words[::2]) #this command outputs words 0,2,4 etc starting fom 0 not 1
#not every second word as the human eye counts
#but that is how the example provided for the problem appears so it must be grand
#I cannot figure out how to format the text to appear without square brackets,commas and parenthesis
#Enter a phrase: python problem set is a wonderful challenge
#['python', 'set', 'a', 'challenge']
