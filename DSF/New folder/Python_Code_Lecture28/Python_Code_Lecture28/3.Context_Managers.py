# Python program creating a context manager

class ContextManager():
	def __init__(self):
		print('init method called')
#The __enter__() returns the resource that needs to be managed		
	def __enter__(self):
		print('enter method called')
		return self
#The __exit__() does not return anything but performs the cleanup operations.	
	def __exit__(self, exc_type, exc_value, exc_traceback):
		print('exit method called')


with ContextManager() as manager:
	print('with statement block')
