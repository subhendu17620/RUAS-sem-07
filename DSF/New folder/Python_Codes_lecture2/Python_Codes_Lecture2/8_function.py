#Define a simple function to add two objects
def addMe2Me(x):
    print('Adding two objects: ')
    return (x + x)

#Call a simple function to add two objects
print(addMe2Me(10))
print(addMe2Me('Python'))
print(addMe2Me([-1, 'abc']))

# #Define a simple function with default argument
# def foo(debug=1):
#     print('determine if in debug mode with default argument')
#     if debug:
#         print ('in debug mode')
#     print ('done')

# #Call a simple function with default argument
# foo()
# foo(0)