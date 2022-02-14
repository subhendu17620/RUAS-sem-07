#This code is used to demonstrate the Try except 
try:
    f = open('blah')
    print ('We can open file')
except IOError:
    print ('could not open file')

#This code is used to demonstrate the Try with multiple except 
def safe_float(object):
    try:
        retval = float(object)
        print('It convert to the float value',retval)
    except ValueError:
        print('could not convert non-number to float')
    except TypeError:
        print('object type cannot be converted to float')

#Call the Function
safe_float('xyz')
safe_float(23.5)
safe_float(673)

#This code is used to demonstrate the Try with Finally
try:
    ccfile = open('carddata.txt')
    try:
        txns = ccfile.readlines()
        print('The content inside the file is: ',txns)
    finally:
        ccfile.close()
        print('The file is closed')
except IOError:
    print('no txns this month\n')

