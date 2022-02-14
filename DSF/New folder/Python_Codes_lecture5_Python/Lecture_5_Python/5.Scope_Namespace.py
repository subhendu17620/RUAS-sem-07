#Scope Vs Namespace: There are either two or three active namespaces. From within a function, 
# the local scope encompasses the local namespace, the first place a name is searched for.
#  If the name exists here, then checking the global scope (global and built-in namespaces) is skipped.
# From the global scope (outside of any function), a name lookup begins with the global
#namespace. If no match is found, the search proceeds to the built-in namespace.

#!/usr/bin/env python
j, k = 1, 2                         #Global Variable

def proc1():
    j, k = 3, 4                     #Local Variable
    print ("Inside Process 1 j == %d and Inside Process 1 k == %d" % (j, k))
    k = 5

def proc2():
    j = 6
    proc1()
    print ("Inside Process 2 j == %d and Inside Process 2 k == %d" % (j, k))

k = 7                           #Global Variable
proc1()
print ("Outside Process 1 j == %d and Outside Process 1 k == %d" % (j, k))

j = 8                           #Global Variable
proc2()
print ("Outside Process 2 j == %d and Outside Process 2 k == %d" % (j, k))
