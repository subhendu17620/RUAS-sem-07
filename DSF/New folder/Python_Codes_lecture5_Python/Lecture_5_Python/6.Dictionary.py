
#Initiate a dictionary object
dict1 = {'name': 'earth', 'port': 80}
print("Content of Dictionary collection is: ", dict1)
print("Access value of a key in a Dictionary collection is: ", dict1['name'])
dict1['name'] = 'venus'     #Update a value of a key
print("Dictionary after a Update: ", dict1)
del dict1['name']           #delete a key
print("Dictionary after deleting a key: ", dict1)

dict2 = {'lang': 'Python', 'howmany': 3}
print('There are %(howmany)d %(lang)s Quotation Symbols' %dict2)
dict2.clear()      #remove all the entries
print("Dictionary after removing all the entries: ", dict2)
del dict2         #Deleting whole dictionary
#print("Dictionary after removing all the entries: ", dict2)