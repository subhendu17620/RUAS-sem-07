#Python is dynamically-type.Therefore, pre decalaration of a variable is not necessary
#i.e. int counter is not neccesary
counter = 0
name = 'Bob'
# Python does not support operators such as counter++ or --counter.
counter = counter + 10
print ("Person name %s run %d km in a marathon" % (name, counter))

#Python is object-oriented.Therefore, do not need to declare variables before using them
#i.e. float miles or miles is not required to reference before it is initialized
miles = 1000.0

#Do not begin an identifier with an underscore. i.e. _kilometers is not allowed  
# as It often used in names of library functions (such as "_main" and "_exit").
kilometers = 1.609 * miles
print ('%f miles is the same as %f km' % (miles, kilometers))
