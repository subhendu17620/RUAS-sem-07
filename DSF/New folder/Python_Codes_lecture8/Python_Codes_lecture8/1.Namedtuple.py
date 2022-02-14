# Python code to demonstrate namedtuple() 
      
from collections import namedtuple 
      
# Declaring namedtuple()  
Student = namedtuple('Student',['name','age','DOB'])  
      
# Adding values  
S1 = Student('Sumit','16','2542005')  
S2 = Student('Vignesh','19','1571997')   

# Access using index  
print ("The Student age using index is : ",end ="")  
print (S1[1])  
      
# Access using name   
print ("The Student name using keyname is : ",end ="")  
print (S2.name)

# Access using getattr()
print ("The Student DOB using getattr() is : ",end ="")
print (getattr(S1,'DOB'))

# using _fields to display all the keynames of namedtuple()
print ("All the fields of students are : ")
print (S1._fields)
  
# using _replace() to change the attribute values of namedtuple
print ("The modified namedtuple is : ")
print(S1._replace(name = 'Manjeet'))