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
s = (input("Hello. Please input a short sentence of 10 words or less. "))
t = s.split()
t[0] = [] 
t[2] = [] 
t[4] = [] 
t[6] = [] 
t[8] = [] 

print (t)
#This code kinda works but returns IndexError: list assignment index out of range
# if the input is less than the #number of elements in the code, if there isn't an eighth
#element for example, needs to be more conditonal
#Also the output is 'ugly'