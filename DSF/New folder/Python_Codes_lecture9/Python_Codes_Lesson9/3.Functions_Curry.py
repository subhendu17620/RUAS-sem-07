# This code is the demonstation of Currying in Python - Many to Single Argument
def change(a):
	def w(b):
		def x(c):
			def y(d):
				def z(e):
					print(a, b, c, d, e)
				return z
			return y
		return x
	return w

# Call the main function
change(10)(20)(30)(40)(50)

# Demonstrate Currying function to convert Days to Seconds
def changeDays2Seconds(b, c, d):
	def a(x):
		return b(c(d(x)))
	return a
	
def daystohour(time):
	""" Function that converts days to hours. """
	return time * 24
	
def hourstominutes(time):
	""" Function that converts hours to minutes. """
	return time * 60
	
def minutestoseconds(time):
	""" Function that converts minutes to seconds. """
	return time * 60
	
if __name__ == '__main__':
	transform = changeDays2Seconds(minutestoseconds, hourstominutes, daystohour)
	e = transform(10)
	print("The days converted to second: ",e)
	
