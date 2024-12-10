# File handling

# File handling in python refers of working with files, which can be used read data from files, write data to files, and perform other operations like renaming, deleting, etc.
# File handling is an important part of web development, as it is used to store data (like user details, product details, etc) in a file.

# In python, file operation takes place in the following order:
# 1. Open a file
# 2. Read or write (perform operation)
# 3. Close the file

# Opening a file
# To open a file in python, we use the open() function. The open() function takes two parameters: filename and mode.

# Syntax:
# file = open("DAY 06\myfile.txt") # open file in current directory
# fileContent = file.read() # read the content of the file and store it in a variable
# print(fileContent) # print the content of the file

# file = open("DAY 06\myfile1.txt") # FileNotFoundError: [Errno 2] No such file or directory: 'DAY 06\\myfile1.txt'  # file does not exist # file name should be matched exactly.

# files are opened in read mode by default, but we can also specify the mode while opening a file.
# There are four modes in which a file can be opened:

# # 1. "r" - Read - Default value. Opens a file for reading, error if the file does not exist.
# file = open("DAY 06\myfile.txt", "r") # open file in current directory

# fileContent = file.read() # read the content of the file and store it in a variable
# print(fileContent) # print the content of the file

# fileContent = file.readline() # read the first line of the file and store it in a variable
# print(fileContent)

# fileContent = file.readlines() # read all the lines of the file and store it in a variable as a list
# print(fileContent)

# file.close() # close the file, it is a good practice to close the file after performing operations on it due to memory management.
# fileContent = file.read() # Can't read from closed file, ValueError: I/O operation on closed file.

# 2. "w" - Write - Opens a file for writing, creates the file if it does not exist.
# file = open("DAY 06\myfile.txt", "w") # "w" - Write - Opens a file for writing.

# 3. "a" - Append - Opens a file for appending, creates the file if it does not exist.
# file = open("DAY 06\myfile.txt", "a") # "a" - Append - Opens a file for appending.

# 4. "x" - Create - Creates the specified file, returns an error if the file exists.

