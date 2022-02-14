# A Python program to return multiple values from a method using tuple(by Default), List and Dictionary

# This function returns a tuple
def learnTuple():
	str = "Core Collection Tuple"
	x = 10
	return str, x; # Return tuple, we could also

# Driver code to test above method
str, x = learnTuple() # Assign returned tuple
print("Retun the String value: ",str)
print("Retun the Integer value: ",x)

# This function returns a list
def learnList():
    str = "Core Collection List"
    x = 20   
    return [str, x];  
  
# Driver code to test above method
list = learnList() 
print("Retun the List value: ",list)

# This function returns a dictionary
def learnDictionary():
    d = dict(); 
    d['str'] = "Dictionary Collection List"
    d['x']   = 30
    return d
  
# Driver code to test above method
d = learnDictionary() 
print("Retun the Dictionary value: ",d)