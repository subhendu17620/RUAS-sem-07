#Named tuples also provide a bunch of cool features that allow you to define default values for your fields, 
# create a dictionary from a given named tuple, replace the value of a given field
from collections import namedtuple,OrderedDict

# Define default values for fields
Person = namedtuple("Person", "name job", defaults=["Python Developer"])
person = Person("Jane")
print(person)

# Create a dictionary from a named tuple
print ("Convert NameTuple into Dictionary: ",end="")
print(person._asdict())
# Replace the value of a field
person = person._replace(job="Web Developer")
print(person)

#Initialize a ordered dictionary
letters = OrderedDict(b=2, d=4, a=1, c=3)
print("The Ordered Dictionary is:",letters)

# Move b to the right end
letters.move_to_end("b")
print("The Ordered Dictionary after moving b to end is:",letters)

# Sort letters by key
for key in sorted(letters):
    letters.move_to_end(key)
print("The sorted Ordered Dictionary is:",letters)