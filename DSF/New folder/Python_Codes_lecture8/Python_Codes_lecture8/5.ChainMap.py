# Python program to demonstrate ChainMap  
            
from collections import ChainMap  
             
d1 = {'a': 1, 'b': 2} 
d2 = {'c': 3, 'd': 4} 
d3 = {'e': 5, 'f': 6} 
    
# Defining the chainmap  
chain = ChainMap(d1, d2, d3)  
print ("The Chaining of three Dictonary are : ",end="")       
print(chain)

# printing chainMap using maps
print ("All the ChainMap contents are : ")
print (chain.maps)
  
# printing keys using keys()
print ("All keys of ChainMap are : ")
print (list(chain.keys()))
  
# printing keys using keys()
print ("All values of ChainMap are : ")
print (list(chain.values()))


# using new_child() to add new dictionary
d4 = {'x': 11, 'y': 12} 
chain1 = chain.new_child(d4)

# displaying value associated with b before reversing
print ("New Chain Map is : ",end="")
print (chain1)

print ("Value associated with a Key b is : ",end="")
print (chain1['b'])