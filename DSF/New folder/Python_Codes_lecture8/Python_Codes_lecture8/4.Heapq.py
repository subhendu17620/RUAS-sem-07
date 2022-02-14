# Python code to demonstrate working of heapq
  
# importing "heapq" to implement heap queue
import heapq
  
# initializing list 
li1 = [6, 7, 9, 4, 3, 5, 8, 10, 18]

# using heapify, list contains the 0th index with the smallest value
print ("The sorted list using heapify() is : ",end="")
heapq.heapify(li1)
print(li1)

#Pop the smallest value and push using the heappushpop method
print ("Pop the smallest value and push using the heappushpop method : ",end="")
print(heapq.heappushpop(li1,11))
print(li1)

#Pop the smallest value and push using the heappushpop method
print ("Pop the smallest value and replace using the heapreplace method : ",end="")
print(heapq.heapreplace(li1,22))
print(li1)

# using nlargest to print 3 largest number
print("The 3 largest numbers in list are : ",end="")
print(heapq.nlargest(3, li1))
  
# using nsmallest to print 3 smallest numbers
print("The 3 smallest numbers in list are : ",end="")
print(heapq.nsmallest(3, li1))


