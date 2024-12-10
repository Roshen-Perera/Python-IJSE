# my_list_1 = ["green","red","blue","cat","dog","apple"]
# my_list_2 = ["adoo"]


# my_list_2 = my_list_1
# # copy the list to another list

# print(my_list_2) # ['green', 'red', 'blue', 'cat', 'dog', 'apple']

# # Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# sports = ("football","cricket","hockey","tennis")
# print(len(sports)) # to find the length of tuple


# animals = ("cat",) # if we want to create a tuple with only one item, we have to add a comma after the item, otherwise Python will not recognize it as a tuple.
# print(type(animals))

# my_tuple = ("apple","banana",30,"mango")

# print(my_tuple[1:3]) # 

# my_tuple_1 = ("apple","banana",30,"mango")
# print(type(my_tuple_1))

# my_list_3 = list(my_tuple_1) # convert tuple to list to change any value
# print(type(my_list_3))
# print(my_list_3)

# my_list_3[0] = "grapes"
# print(my_list_3)

# my_tuple_2 = tuple(my_list_3) # convert list to tuple


# #When we need to remove an element from a tuple, we convert it into a list and then remove the element and convert it back to a tuple.
# tuple1 = (10,20,30,40)
# print(tuple1)

# list1 = list(tuple1) # convert tuple to list
# list1.pop(2)

# print("after removing the element from the list: ",list1)

# tuple1 = tuple(list1) # convert list to tuple
# print("after converting list to tuple: ",tuple1)
# print(type(tuple1))
 
# # When we need to sort the elements of a tuple, we convert it into a list, then sort the elements and convert it back to a tuple.
# tuple2 = (60, 20, 30, 70)
# print(tuple2)

# list2 = list(tuple2) # convert tuple to list
# list2.sort()

# tuple2 = tuple(list2) # convert list to tuple
# print(tuple2) # sorted tuple

# #Nested Tuples are tuples that contain other tuples.

# nested_tuple = ((1, 10, 8), ("apple", "banana", "cherry"), (True, False))
# print(nested_tuple[0][1]) # to access the element of nested tuple

# ## Python Range
# # Range is a sequence of numbers, it is used to iterate over with for loops. It is a built-in function that generates the integer numbers between the given start integer to the stop integer.

# s_1 = range(2, 15, 3) # start, stop, step
# print(s_1, type(s_1))

# ##Dictionaries are used to store data values in key:value pairs.
# # A dictionary is a collection which is unordered, changeable and indexed. 
# In Python dictionaries are written with curly brackets, and they have keys and values.

# dict_1 = {
#     "name": "sugar",
#     "weight": "1kg",
#     "price": "120.25",
# }

# print(dict_1) 

# print(dict_1["name"]) # access the value of key

# dict_1.update({"name": "salt"}) # update the value of key
# dict_1.update({"weight": "2kg"}) # update the value of key
# dict_1.update({"price": "150.25"}) # update the value of key

# dict_1["quantity"] = "10" # add new key value pair

# # dict_1.pop("price") # remove the key value pair

# print(dict_1)

# dict_1.popitem() # remove the last key value pair
# print(dict_1)

# thisDict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }

# thisDict["brand"] = "Toyota" # change the value of key

# print(thisDict)

# thisDict_copy = thisDict # copy the dictionary
# print(thisDict_copy)

# thisDict_copy["year"] = 2020 # change the value of key
# print(thisDict_copy)

# # Use thisDict["key"] = value when you want a simple, direct assignment or update for a single key.
# # Use thisDict.update({...}) when you need to update multiple key-value pairs at once.

## Arithmetic Operators
# These operators perform arithmetic operations on numeric values.

#  
## Inputs
# We can use the input() function to take input from the user. The input() function reads a line from input, converts it into a string, and returns it.

# x = int(input("Enter the value of x: ")) # take input from user

# if x % 7 == 0: # check the value of x is divisible by 7 or not
#     print("Value of X is divisible by 7")
# else:
#     print("Value of X is not divisible by 7")

# # Conditional Statements in Python should be indented with 4 spaces. If you use a tab, it will throw an error.

# # Logical Operators
# # Logical operators are used to combine conditional statements.

# x = 15
# y = 5

# print(x > 10 and y < 10) # returns True because 10 is greater than 10 and 5 is less than 10
# print(x > 10 and y > 10) # returns False because 10 is greater than 10 but 5 is not greater than 10

# print(x > 10 or y < 10) # returns True because 10 is greater than 10 and 5 is less than 10
# print(x < 10 or y < 10) # returns True because 10 is not greater than 10 but 5 is less than 10

# print((x > 10 and y < 10)) # returns True because 15 is greater than 10 and 5 is less than 10 but it returns the opposite value which is False because of not operator

## Identity Operators
# Identity operators are used to compare memory locations of two objects. They determine whether the two objects are the same object memory.


# ## Membership Operators
# # Membership operators are used to test if a value is presented in an object.

# nums = [1, 2, 3, 4, 5]

# print(1 in nums) # returns True because 1 is present in the list
# print(6 in nums) # returns False because 6 is not present in the list

# ### Control Flow Statements

# ## If Statement
# # The if statement is used to execute a block of code only if the condition is True.

# n = 12
# if n % 2 == 0: # if the condition is True
#     print("Even Number")
# else: # if the condition is False 
#     print("Odd Number")

# o = 15
# if o > 10: # if the condition is True
#     print("Greater than 10") # 
# elif o < 10: # if the condition is False
#     print("Less than 10")
# else: # if the condition is False
#     print("Equal to 10")


# marks = int(input("Enter your marks: "))


# if 85 <= marks <= 100:
#     print("A")
# elif 75 <= marks < 85:
#     print("B")
# elif 65 <= marks < 75:
#     print("C")
# elif 55 <= marks < 65:
#     print("D")
# elif 0 <= marks < 55:
#     print("F")
# else:
#     print("Invalid Marks")

# x = 10
# y = 6
# z = 30


# if x > y and x > z:
#     print("X is the largest number")
# elif y > x and y > z:
#     print("Y is the largest number")
# else:
#     print("Z is the largest number")    