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

# #1. "r" - Read - Default value. Opens a file for reading, error if the file does not exist.
# file = open("DAY 06\myfile.txt", "r") # open file in current directory

# fileContent = file.read() # read the content of the file and store it in a variable
# print(fileContent) # print the content of the file

# fileContent = file.readline() # read the first line of the file and store it in a variable
# print(fileContent)

# fileContent = file.readlines() # read all the lines of the file and store it in a variable as a list
# print(fileContent)

# file.close() # close the file, it is a good practice to close the file after performing operations on it due to memory management.
# fileContent = file.read() # Can't read from closed file, ValueError: I/O operation on closed file.

# 'with' keyword
# The 'with' keyword is used to simplify exception handling in python. 
# It is used to wrap the execution of a block of code within methods defined by the context manager.

# # 2. "w" - Write - Opens a file for writing, creates the file if it does not exist.
# file = open("DAY 06\myfile.txt", "w") # "w" - Write - Opens a file for writing.
# file.write("Hello, World!") # write the content to the file
# file.close() # close the file
# If there are any content in the file, it will be overwritten.

# # 3. "a" - Append - Opens a file for appending, creates the file if it does not exist.
# file = open("DAY 06\myfile.txt", "a") # "a" - Append - Opens a file for appending. The text will be added at the end of the file.
# file.write("Hello, World!") # write the content to the file

# 4. "x" - Create - Creates the specified file, returns an error if the file exists.

# Syntax:
# with open("DAY 06\myfile.txt", "r") as file:
#     fileContent = file.read() # read the content of the file and store it in a variable
#     print(fileContent) # print the content
#     # No need to close the file, it will be closed automatically.

# Resourse Management: Using with ensures that the file is properly closed after its operation completes, preventing issues like file locks, resource leaks, or data corruption.

# Exercise:
# 1. Create a file named 'wtext.txt' and write the following content to it:
# with open("DAY 06\\text.txt", "w") as file:
#     # file.write("Hello, World!, This our python class.")
#     # file.write("Hello my name is John Doe.") # overw the content of the file
#     nameList = ["Hello world!\n", "This is our python class.\n", "Hello my name is John Doe.\n"] # write multiple lines to the file using list
#     file.writelines(nameList)

# with open("DAY 06\\text.txt", "a") as file:
#     file.write("Hello, World!") # append the content to the file


## EXERCISE 02
# Create a program that stores and manages contact details in a file named contacts.txt.
# Each contact entry should include the following details: name, phone number, and email address.
# The program should support the following operations:
# 1. Add a new contact : Append the contact details to the file.
# 2. List all contacts : Display all the contact details in the file.
# 3. Clear all contacts : Remove all the contact details from the file.

# while True:
#     print("Contacts Mangement\nEnter 1 to add a contact\nEnter 2 view contacts\nEnter 3 to exit")
#     option = int(input("\nEnter an option: "))
#     if(option == 1):
#         name = input("Enter Name: ")
#         email = input("Enter Email: ")
#         number = input("Enter Contact No: ")
#         details = [name,"\n", email,"\n", number,"\n"]
#         with open("DAY 06\\contact.txt", "a") as file:
#             file.writelines(details)
#     elif(option == 2):
#         with open("DAY 06\\contact.txt", "r") as file:
#             contactRead = file.read()
#             print(contactRead)
#     elif(option == 3):
#         print("Bye")
#         break

# What is JSON ?
# JSON (JavaScript Object Notation) is a lightweight data-interchange format that is easy for humans to read and write and easy for machines to parse and generate.
# JSON is a text format that is completely language independent but uses conventions that are familiar to programmers of the C-family of languages, including C, C++, C#, Java, JavaScript, Perl, Python, and many others.
# JSON is built on two structures:
# 1. A collection of name/value pairs. In various languages, this is realized as an object, record, struct, dictionary, hash table, keyed list, or associative array.
# 2. An ordered list of values. In most languages, this is realized as an array, vector, list, or sequence.

#JSON is often used to transmit data between a server and a web application.

# JSON vs Dictionary
# JSON is similar to a dictionary in python, but there are some differences between them:
# 1. JSON keys are always strings, while dictionary keys can be any immutable data type.
# 2. JSON values can be strings, numbers, arrays, objects, booleans, or null, while dictionary values can be any data type.
# 3. JSON uses double quotes for key and value pairs, while dictionary uses single quotes for keys.

# JSON in Python
# Python has a built-in package called json, which can be used to work with JSON data.
# The json package has two main functions:
# 1. json.dumps() - Converts a python object into a json string.
# 2. json.loads() - Converts a json string into a python object.

import json

# # Specify the path of the JSON file
# json_file_path = "DAY 06\\test.json"

# # Open the JSON file for reading
# with open(json_file_path, "r") as file:
#     # Load the JSON data from the file
#     data = json.load(file)
#     # Print 'data' contains the contents of the JSON file as a Python dictionary
#     print(data) # {'name': 'John Doe', 'age': 30, 'city': 'New York'}
#     # Print the type of 'data'
#     print(type(data)) # <class 'dict'>

# test = {
#     "fruit": "Apple",
#     "size": "Large",
#     "color": "Red"
# }

# # Convert the Python dictionary to a JSON string
# json_string = json.dumps(test)
# # Print the JSON string
# print(json_string) # {"fruit": "Apple", "size": "Large", "color": "Red"}
# print(type(json_string)) # <class 'str'>

# with open("DAY 06\dump.json", "w") as json_file:
#     # Write the JSON data to the file
#     json.dump(test, json_file, indent=4)




# You are give student details in student.JSON which contain information about and there grades, your tast is to
# 1. Read the JSON file and print the content.
# 2. Display the name of all Students who scored above 75.
# 3, Add a new student to the JSON file.
# 4. Save the updated data to the Json File

# with open("DAY 06\student.json", "r") as json_file:
#     data = json.load(json_file)
#     print(data)
#     print(type(data))

#     for student in data:
#         if student['grade'] > 75:
#             print(student['name'])
    

# name = input("Enter name: ")
# grade = int(input("Enter grade: "))

# newEntity = {
#     "name": name, 
#     "grade": grade
# }

# with open("DAY 06\student.json", "w") as json_file:
#     data.append(newEntity)
#     json.dump(data,json_file,indent=4)

# What is CSV ?
# CSV (Comma Separated Values) is a simple file format used to store tabular data, such as a spreadsheet or database.
# CSV files are plain text files that contain data separated by commas or other delimiters.
# Each line of the file is a data record, and each record consists of one or more fields, separated by commas or other delimiters.

# import csv

# csv_file_path = "DAY 06\customers-100.csv"

# with open(csv_file_path, "r", newline="") as csv_file:
#     # Create a CSV reader object
#     csv_reader = csv.reader(csv_file)
    
#     print(csv_reader, type(csv_reader))
#     for row in csv_reader:
#         print(row, type(row))

# csv_file_path = "DAY 06\output.csv"

# data = [ 
#     {"Name": "Roshen", "Age": 19, "City": "Avissawella"},
#     {"Name": "John", "Age": 20, "City": "Colombo"},
#     {"Name": "Doe", "Age": 21, "City": "Kandy"}
# ]

# fieldnames = ["Name", "Age", "City"]

# # Open the CSV file for writing
# with open(csv_file_path, "w", newline="") as csv_file:
#     # Create a CSV writer object
#     csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#     # Write the header (column names) to the CSV file
#     csv_writer.writeheader()
#     # Write the data to the CSV file
#     for row in data:
#         csv_writer.writerow(row)
#         print(row, type(row))

# print(f"Data written to {csv_file_path}")

# with open(csv_file_path, "w", newline="") as csv_file:
#     # Create a CSV writer object
#     csv_writer = csv.writer(csv_file)
#     # Write the header
#     csv_writer.writerow(data)

# Nested Function
# A function defined inside another function is called a nested function.
# Nested functions are used to perform a specific task within the main function.
# Nested functions can access variables from the enclosing function, but they cannot modify them.

# def outer_function(x):
#     def inner_function(y): 
#         return x + y
#     return inner_function

# add = outer_function(10) # add is a function object that takes one argument and returns the sum of the argument and 10. Its similair to 10 + y
# print(add(10)) # 20. The inner function is called with the argument 10, which is added to the value of x (10) and returned.

# Passing a Function as an Argument
# A function can be passed as an argument to another function.
# This is useful when you want to perform different operations on the same data.
# The function that accepts another function as an argument is called a higher-order function.

# def add(x, y):
#     return x + y

# def calculate(func, x, y):
#     return func(x, y)

# result = calculate(add, 10, 20)

# print(result) # 30

# Python Decorators
# A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure.
# Decorators are usually called before the definition of a function you want to decorate.
# Decorators are used to modify the behavior of a function or a class method.
# Decorators are functions that take another function as an argument and return a new function.

# def make_pretty(func):
#     def inner():
#         print("I got decorated")
#         func()
#     return inner

# def ordinary():
#     print("I am ordinary")  

# get_decorated = make_pretty(ordinary) # the function ordinary is passed to the make_pretty function as an argument, and the returned function is assigned to the variable get_decorated.
# get_decorated() # I got decorated I am ordinary


# @make_pretty is a decorator that is used to modify the behavior of the ordinary function.
# The @ symbol is used to apply the decorator to the function.

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty # the make_pretty decorator is applied to the ordinary function.
def ordinary():
    print("I am ordinary")

ordinary() # I got decorated I am ordinary

# Create a decorator checks_positive that checks if the input via a function is positive or not.
    # If input is not positive, print "Input is must be positive" and return None.

# Use this decorator on function calculate_square_root that:
    # Takes a number as input
    # Returns the square root of the input number

import math

def checks_positive(func): # decorator
    def inner(x) : # inner function
        if x < 0: # check if the input is positive
            print("Input must be positive")
            return None
        else:
            return func(x) # this will return the square root of the input number
    return inner # return the inner function that checks if the input is positive
@checks_positive # apply the checks_positive decorator to see if the input is positive
def calculate_square_root(num): # function that calculates the square root of the input number
    return math.sqrt(num) # return the square root of the input number

# num = int(input("Enter a number: "))
print(calculate_square_root(16))