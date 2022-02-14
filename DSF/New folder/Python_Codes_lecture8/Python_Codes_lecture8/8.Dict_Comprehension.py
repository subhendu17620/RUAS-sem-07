#The demonstration is to create a Dictionary
numbers = range(10)
new_dict_for = {}

# Add values to `new_dict` using for loop
for n in numbers:
    if n%2==0:
        new_dict_for[n] = n**2
print ("The dictionary created : ",end="")
print(new_dict_for)



#The demonstration is to create Dictionary Comprehension with existing Dictionary
new_dict_comp = {n:n**2 for n in numbers if n%2 == 0}
print ("The dictionary Comprehension created : ",end="")
print(new_dict_comp)


dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# Double each value in the dictionary using Dictionary Comprehension
double_dict = {k:v*2 for (k,v) in dict.items()}
print ("The modified dictionary which double the values created using dictionary Comprehension is : ",end="")
print(double_dict)

# Apply Multiple IF condition using Dictionary Comprehension
dict_doubleCond = {k:v for (k,v) in dict.items() if v>1 if v%2 == 0}
print ("The modified dictionary after multiple IF condition using dictionary Comprehension is : ",end="")
print(dict_doubleCond)

