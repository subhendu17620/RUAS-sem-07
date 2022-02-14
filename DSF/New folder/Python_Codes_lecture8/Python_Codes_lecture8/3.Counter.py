# A Python program to demonstrate working of Counter
from collections import Counter

my_str = "Welcome to Python for Data Science!"
print("The number of words in the String are: ",Counter(my_str))

list1 = ['x','y','z','x','x','x','y','z']
print("The value of x, y, z in the List are: ",Counter(list1))

dict1 =  {'x': 4, 'y': 2, 'z': 2, 'z': 2}
print("The value of x, y, z in the Dictionary are: ",Counter(dict1))

tuple = ('x','y','z','x','x','x','y','z')
print("The value of x, y, z in the Tuple are: ",Counter(tuple))

#Initialize a counter
_count = Counter()
_count.update('Welcome to Python for Data Science!')
print('%s : %d' % ('u', _count['c']))
print('\n')
for char in 'Python':
    print('%s : %d' % (char, _count[char]))

#Update a counter
counter1 =  Counter({'x': 5, 'y': 12, 'z': -2, 'x1':0})
counter2 = Counter({'x': 2, 'y':5})
counter1.update(counter2)
print(counter1)