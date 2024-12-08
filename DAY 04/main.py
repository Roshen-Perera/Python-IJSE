# Aribitrary positional arguments

# Arbitrary positional arguments are used when you don't know how many arguments will be passed to a function.

# def arbitrary_positional_args(*args):
#     print(args, type(args))# args is a tuple

# arbitrary_positional_args(1, 2, 3, 4, 5)# (1, 2, 3, 4, 5) <class 'tuple'>

# def arbitrarySum(*args):
#     # sum = 0
#     # for i in args:
#     #     sum += i
#     # return sum
#     return sum(args)

# print(arbitrarySum(1, 2, 3, 4, 5))# 55  

# Summarize grades that accepts a student name as a mandotory argument and an arbitrary number of grades scored by the student.
# The function should print student name 
# Calculate and print the highest grade, lowest grade and average
# If ko grades it should print no grade provided.

# def summarize_grades(name, *grades):
#     print("Name: ",name)
#     if not grades:
#         print("No grades provided")
#     else:
#         print("Maximum grade: ",max(grades))
#         print("Minimum grade: ",min(grades))
#         print("Sum of the grades: ",sum(grades))
#         print("Average of the grades: ",sum(grades)/len(grades))

# summarize_grades("Roshen", 80, 60)
# summarize_grades("Roshen")

# def arbitrary_keyword_args(**kwargs): # **kwargs is used to pass a keyworded, variable-length argument list
#     print(kwargs, type(kwargs))# kwargs is a dictionary
#     for key, value in kwargs.items():
#         print(key, value)

# arbitrary_keyword_args(name="Roshen", age=25, city="Colombo")# {'name': 'Roshen', 'age': 25, 'city': 'Colombo'} <class 'dict'>

# write a python function call employee_info() that accepts a required name parameters and arbitrary number of keyword arguments representing additional details about the employee the function should, print the employess name iterate through the keyword arguments and print each key value pair in the format.
# return a dictionary with all employee details

# def employee_info(name, **empinfo):
#     print("Employee Name: "+name)
#     for key, value in empinfo.items(): 
#         print(key, value)

#     empinfo["name"] = name
#     print(empinfo)

# employee_info("Roshen", age = 18, address = "avissawella")

# Absolute value of a number
# Absolute value is the positive value of a number without considering its sign.

# map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)

# def find_square(num):
#     return num ** 2

# numbers = [1, 2, 3, 4, 5]

# squared = map(find_square, numbers)
# print(list(squared), type(squared))# [1, 4, 9, 16, 25] # list is used because map object is an iterator

# myList = [1,2,3,4,5]

# def find_square(num):
#     return num*num

# result = map(find_square,myList)
# print(result,type(result))

# result = list(result)
# print(result,type(result))

# we can pass multiple iterables to the map function
# map(function, iterable1, iterable2, iterable3,...)

# myList1 = [10,12,7,5]
# myList2 = [9,5,4,1]

# def listSum(num1,num2):
#     return num1+num2

# result = map(listSum,myList1,myList2)
# print(result,type(result))

# result = list(result)
# print(result,type(result))

# You have a list of integers representing temperatures in celsius.
# temp_list = [20 30 35 40 50]
# Write a python function that accepts a list of temperatures in celsius and returns a list of temperatures in fahrenheit.
# The formula to convert celsius to fahrenheit is f = c * 9/5 + 32

# temp_list = [20, 30, 35, 40, 50]

# def celsius_to_fahrenheit(celsius): 
#     return celsius * 9/5 + 32

# temp = map(celsius_to_fahrenheit, temp_list)
# print(temp, type(temp))

# temp = list(temp)
# print(temp, type(temp))
    
# filter() function returns an iterator were the items are filtered through a function to test if the item is accepted or not.
# It filters the original iterable and returns the items that return True for the function.

# filter(function, iterable)
#           ^
#         logical 
#        true/false

# numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def is_even(num):
#     return num % 2 == 0

# evenNumbers = filter(is_even, numberList)
# print(evenNumbers, type(evenNumbers))

# evenNumbers = list(evenNumbers)
# print(evenNumbers, type(evenNumbers))

# Python lambda function
# A lambda function is a small anonymous function. 
# A lambda function can take any number of arguments, but can only have one expression.

# lambda arguments : expression
# lambda: is a keyword
# arguments: are the input parameters
# expression: is the output that is returned after the function is called

# add = lambda x, y : x + y

# print(add(5, 3))# 8

# write a python that : 
# 	takes a list of tupels,whre is each tuple contails a name (string)
# 	use a lambda function to filture up the tuple where the age is less than 18
# 	print  a list of tuples after filter

# people = [("John", 25), ("Jane", 16), ("Doe", 30), ("Harry", 17)]

# filtered = filter(lambda x: x[1] < 18, people) # x[1] is the age in the tuple
# print(list(filtered))

# Why use lambda functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.
# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

# Create a lambda function that returns the maximum number.

# findMax = lambda a,b : a if a > b else b
# print(findMax(5, 8))


# def find_factorial(x):
#     fact = 1
#     for i in range(1, x+1):
#         fact = fact*i
#     return fact

# print(find_factorial(5))

# def factorial(x):
#     if x == 0 or x == 1:
#         return 1
#     else:
#         return x*factorial(x-1)

# print(factorial(2000))

# create a function recursive which prints the sum of a list



# reList = [5, 8, 3, 6, 2]

# def recursiveSum(reList):
#     if not reList:
#         return 0
#     else:
#         return reList[0] + recursiveSum(reList[1:])

# print(recursiveSum(reList))

# ## WHat are python modules?
# # A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended.
# # A module can define functions, classes, and variables. A module can also include runnable code.

# import math

# math.sqrt(25)# 5.0
# math.factorial(5)# 120

# print(math.pi)

