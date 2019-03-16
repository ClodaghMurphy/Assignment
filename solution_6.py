#Write a program that takes a user input string and outputs every second word.
#Clodagh Murphy 16032019

#Preparation work using exercises from How to Think Like a Computer Scientist by Allen Downey

t = ['a', 'b', 'c']
x = t.pop(1)
print (t)
print (x)

#pop modifies the list and returns the element that was removed. If you don’t provide an
#index, it deletes and returns the last element.

#t = ['i', 'would', 'like', 'to', 'go', 'for', 'a', 'walk']
#x = t.pop(1,3,5,7)
#print (t)
#print (x)
#result TypeError: pop() takes at most 1 argument (4 given)

t = ['i', 'would', 'like', 'to', 'go', 'for', 'a', 'walk']
del t[1:5]
print (t)

s = 'pining for the fjords'
t = s.split()
print (t)

fruitlist = ["apple", "banana", "cherry", "durian", "orange"]
print( fruitlist ) 
fruitlist[1:3] = [] 
print( fruitlist )

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

s = (input("Hello. Please input a sentence of 11 words. ")) 
fruitlist = s.split()
#del is a keyword that allows you to delete a list element, or list slice, by index.
#every time an element is deleted, the code runs again and the element's location on the list
#changes
#Again this is code only works on a list with 11 words and output is ugly
#not much use!
del fruitlist[0] 
del fruitlist[1] 
del fruitlist[2] 
del fruitlist[3] 
del fruitlist[4] 
del fruitlist[5]

print( fruitlist )
