"""
 
"""
import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
for arg in sys.argv:
  print(arg)

# Print out the OS platform you're using:
# YOUR CODE HERE
print("platform:", sys.platform)

# Print out the version of Python you're using:
# YOUR CODE HERE
print("python version:", sys.version)


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print("process id:", os.getpid())

# Print the current working directory (cwd):
# YOUR CODE HERE
print("cwd:", os.getcwd())

# Print out your machine's login name
# YOUR CODE HERE
print('login name:', os.getlogin())
