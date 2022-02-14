# A Python program to run Lambda Function using the normally defined function
def cube(y):
	return y*y*y
# using the Lambda function
lambda_cube = lambda y: y*y*y


print("Print Cube output using Normal Function: ",cube(5))

# using the lambda function
print("Print output using Lambda Function: ",lambda_cube(5))

# Print List of people above 18 yrs
ages = [13, 90, 17, 59, 21, 60, 5]
adults = list(filter(lambda age: age>18, ages))
print("Print List of people above 18 yrs: ",adults)

# Python code to illustrate map() with lambda() to get double of a list.
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(map(lambda x: x*2, li))
print("lambda function to double values of a list: ",final_list)

# using the lambda function for loop and List Comprehension
tables = [lambda x=x: x*10 for x in range(1, 4)]
for table in tables:
	print("lambda function for List Comprehension: ",table())


