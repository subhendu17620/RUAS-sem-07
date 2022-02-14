#A generator-function generate a value, it does so with the yield keyword rather than return.

def simpleGeneratorFunction():
	yield 1			
	yield 2			
	yield 3			

# Driver code to check above generator function
for value in simpleGeneratorFunction():
	print("Print the values: ",value)
# A Python program to demonstrate use of
# generator object with next()

# x is a generator object
x = simpleGeneratorFunction()

# Iterating over the generator object using next
print("Print the first values: ",x.__next__()) 
print("Print the Second values: ",x.__next__())
print("Print the Third values: ",x.__next__())
