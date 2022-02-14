#This module is to explain further about the built in function of python like str(), type(),
#int(), long(), float(), and complex()
print ("Convert numbers into strings: ",str(0xFF))
print ("Convert Float into Integer: ",int(4.25555))
print ("Convert numbers into Float: ",float(42))
print ("Convert numbers into Complex: ",complex(4))
print ("Creating a Complex: ",complex(4,-9))

#Python has four operational built-in functions for numeric types: abs(), divmod(),
# pow(), and round().
print ("abs() returns the absolute value of the given argument: ",abs(-1.2))
print ("divmod() returns the pair (quotient, remainder) as a tuple: ",divmod(10,3))
print ("Both pow() and the double star ( ** ) operator perform exponentiation: ",pow(2,5))
print ("round() normally rounds a floating point number to the nearest integral number: ",round(3.4999999,1))

#Built in functions for String and Membership (in, not in) to tell where character appear in a String
print ("Length of a string: ",len('Hello Python'))
print ("Max of a string: ",max('HelloPython'))
print ("Min of a string: ",min('Hello Python'))
print ('c' in 'abcd')
print ('n' in 'abcd')
print ('n' not in 'abcd')
