# Import PurePath class from pathlib module
from pathlib import PurePath, Path

# Path
path = '/usr/local/ bin'

# Instantiate the PurePath class
obj = PurePath(path)
print(obj)
# Check whether the given path is absolute or not
isAbs = obj.is_absolute()
print(isAbs)

# Get the current working directory name
cur_dir = Path.cwd()
print(cur_dir)
# Check if path refers to directory or not 
obj2 = Path(path)
print(obj2.is_dir())