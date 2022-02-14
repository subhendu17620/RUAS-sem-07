#Create a List with "a" word in the items and append it
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print ("The List created is : ",end="")
print(newlist)

#The same List is created using List Comprehension with one line of code only
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
list_compr = [x for x in fruits if "a" in x]
print ("The List created using List Comprehension is : ",end="")
print(list_compr)
newlist_compr = [x for x in fruits if x != "apple"]
print ("The List created using List Comprehension without apple is : ",end="")
print(newlist_compr)

newlist_upper = [x.upper() for x in fruits]
print ("The List created using List Comprehension with Upper Case is : ",end="")
print(newlist_upper)

newlist_same = [x for x in fruits]
print ("The List created using List Comprehension as it is : ",end="")
print(newlist_same)

newlist_banana = [x if x != "banana" else "orange" for x in fruits]
print ("The List created using List Comprehension replacing Orange with Banana : ",end="")
print(newlist_banana)