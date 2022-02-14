# Python program to explain os.getcwd() method
         
# importing os module
import os
     
# Get the current working directory (CWD)
cwd = os.getcwd()
     
# Print the current working directory (CWD)
print("Current working directory:", cwd)

# Get the list of all files and directories
# in the root directory
path = "/"
dir_list = os.listdir(path)
 
print("Files and directories in '", path, "' :")
 
# print the list
print(dir_list)