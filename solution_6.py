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

s = (input("Hello. Please input a short sentence of 10 words or less. "))
t = s.split()
print (t)
