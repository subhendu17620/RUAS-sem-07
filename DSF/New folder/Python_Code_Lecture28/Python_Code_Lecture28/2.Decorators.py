#Create a Decorator Method using the inbuilt Functions 
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper

#Assign the Decorator
@uppercase_decorator
def decorating_python():
    return 'Assignment is submitted'

#Print the content
print(decorating_python())

def split_string(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper

#Assign the Decorator
@split_string
@uppercase_decorator
def multiple_decorators_python():
    return 'start preparing for your final exam'

#Print the content
print(multiple_decorators_python())