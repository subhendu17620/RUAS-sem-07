#Demonstrate a Class

class FooClass:
    print('my very first class: FooClass')
    version = 0.1 # class (data) attribute
    
    def __init__(self, nm='John Doe'):
        print('constructor')
        self.name = nm # class instance (data) attribute
        print ('Created a class instance for', nm)

    def showname(self):
        print('display instance attribute and class name')
        print ('Your name is', self.name)
        print ('My name is', self.__class__)# full class name

    def showver(self):
        print('display class(static) attribute')
        print (self.version) # references FooClass.version

    def addMe2Me(self, x): # does not use 'self'
        print('Add two objects')
        return (x + x)

#Create a instance of Fooclass
foo1 = FooClass()

#Create a argument instance of Fooclass
foo1 = FooClass("Ramiah University")

#Call the methods of Fooclass
foo1.showname()
foo1.showver()
print (foo1.addMe2Me(25))
print (foo1.addMe2Me('Hello Python'))
 