
 #!/usr/bin/env python

#This method is used to check whether a number is integer, float, complex number
def displayNumType(number):
    print (number, "is",)
    if type(number) == type(0):
        print ('an integer')
    elif type(number) == type(0.0):
        print ('a float')
    elif type(number) == type(0+0j):
        print ('a complex number')
    else:
        print ('not a number at all!!')

#call the method
displayNumType(-69)
displayNumType(98.6)
displayNumType(-5.2+1.9j)
displayNumType('xxx')
