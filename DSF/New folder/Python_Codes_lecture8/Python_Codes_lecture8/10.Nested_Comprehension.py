# The demonstration is for the simple nested loop in python
matrix = []
for i in range(5):	
	# Append an empty sublist inside the list
	matrix.append([])
	for j in range(5):
		matrix[i].append(j)
print ("The simple Nested loop : ",end="")		
print(matrix)

# The demonstration is for the Nested Comprehension

# Nested list comprehension
matrix = [[j for j in range(5)] for i in range(5)]
print ("The Nested Comprehension loop : ",end="")	
print(matrix)

# 2-D List of planets
planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']] 
flatten_planets = []
for sublist in planets:
    for planet in sublist:
        if len(planet) < 6:
            flatten_planets.append(planet)
print ("The simple Nested loop for Planets is : ",end="")	          
print(flatten_planets)

# Nested List comprehension with an if condition
flatten_planet_loop = [planet for sublist in planets for planet in sublist if len(planet) < 6]
print ("The Nested Comprehension for Planets using Loop is : ",end="")	
print(flatten_planet_loop)