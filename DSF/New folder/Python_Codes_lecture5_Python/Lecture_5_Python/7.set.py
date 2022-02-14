#Initiate a set object
set1={1,2,3,4,5,"hello","tup"}
print("Print collection of set: ",set1)
set1.add("python") #Adding element in collection of set
print("Updated collection of set after adding element: ",set1)
#print("Accesss element from set1",set1[0])   #sets are unordered, so it doesnot support indexing
set1.pop()  # removes random element from the set
print("Updated collection of set after removing element: ",set1)


set2={1,8,"python",7,"python"}      #Duplicates Not Allowed
print("Duplicate elements are not allowed in set: ",set2)