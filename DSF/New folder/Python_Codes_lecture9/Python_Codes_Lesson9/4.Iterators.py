# This code is the demonstation of Iterators using Itr method and next method
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print("My first element: ",next(myit))
print("My second element: ",next(myit))
print("My third element: ",next(myit))

#This code is the demostration of Itertools, which is an built-in Python module that contains 
# functions to create iterators for efficient looping

from itertools import count, cycle

#Create a sequence from 1 to 11 using count function
sequence = count(start=0, step=1)
while(next(sequence) <= 10):
    print("The sequence are ",next(sequence))

#Create a menu using cycle function
dessert = cycle(['Icecream','Cake','Candy'])
count = 0
while(count != 4):
    print('Q. What do we have for dessert? A: ' + next(dessert))
    count+=1