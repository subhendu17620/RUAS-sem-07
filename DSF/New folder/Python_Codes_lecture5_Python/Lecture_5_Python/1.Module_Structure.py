#usr/bin/en python       (1) Startup Line 
print("This is the Module Documentation to explain a formal style of python programming")   # (2) Module Documentation 
import sys                                  # (3) Module imports
                                                 

debug = 1                                       # (4) Gobal Variable Declaration

class FooClass:                                 # (5) Class Declaration
    print('class: FooClass')
    def fooMethod(self):                                  
        print('FooClass Function')

def seperateFunction():                           # (6) Function Declaration                               
    print('seperate Function')
    if debug:
        print('Debug Variable Found')

if __name__ == '__main__':                      # (7) "main" body Declaration
    seperateFunction()
    print('Python System Version: ', sys.version)
    foo = FooClass()
    foo.fooMethod()
    


        
   