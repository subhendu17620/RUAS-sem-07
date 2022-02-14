#This code is used to demonstrate a customize exception
class DemoException(Exception):
    def __init__(self, message):
        super().__init__(message)
        
message = "Exception Triggered! Something went wrong."
print(message)


try:
    raise DemoException(message)
    print("Code Works Fine")
except DemoException:
    print("Demo Exception occurs")