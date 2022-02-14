# import required modules
import inspect
import math
import collections

# create class
class A(object): pass

# use isclass()
print(inspect.isclass(A))

 
# use ismodule()
print(inspect.ismodule(math))

# use ismethod()
print(inspect.ismethod(collections.Counter))
