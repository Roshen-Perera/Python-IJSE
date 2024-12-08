# Creating an object of the class

# parrot_1 = Parrot()
# 
# This will create an object of the class Parrot and assign it to the variable parrot_1.
# 
# The python self
# 
# self represents the instance of the class. By using the "self" keyword we can access the attributes and methods of the class in python.
# It binds the attributes with the given arguments. 

# class Car:
#     category = "Vehicle"    

#     def __init__(self, model, color):
#         self.model = model
#         self.color = color

#     def display(self):
#         print(self.model, self.color)

# new_car = Car("Audi", "Black")
# new_car.display()

# def__init__(self, name, color):

# The __init__ method is similar to constructors in python. Constructors are used to initialize the object's state.
# We use the __init__ method to initialize the object's state. It is run as soon as an object of a class is instantiated.

# class Car:
#     category = "Vehicle"    

#     def __init__(self, model, color):
#         self.model = model
#         self.color = color

#     def display(self):
#         print(self.model, self.color)

#     def update(self, model, color):
#         self.model = model
#         self.color = color    

# new_car = Car("Audi", "Black")
# new_car.display()

# new_car.update("BMW", "White")
# new_car.display()

# #Class Attributes

# print(Car.category)


# Create a class name "Bank Account" with the following attributes:
# 1. account_holder, to store the name of the account holder
# 2. balance, to store the amount in the account initialized to 0

# Add the following methods to the class
# 1. deposit(amount) method to add the amount to the balance
# 2. withdraw(amount) method to subtract the amount from the balance if sufficient balance is available otherwise print "Insufficient Balance"
# 3. display() method to display the current balance

# Write a small script to demontrate the following: 
# 1. Create an object of the class Bank Account
# 2. Perfom deposit, and withdraw operations
# 3. Display the balance after each operation

# class BankAccount:
#     account_holder = "Roshen Perera"
#     balance = 0

#     def __init__(self, account_holder, amount):
#         self.account_holder = account_holder
#         self.balance = amount

#     def deposit(self,amount):
#         if(amount < 0):
#             print("Invalid Amount !!!")
#         else:  
#             print("Deposited: ",amount)
#             self.balance = self.balance + amount
#             return self.balance

#     def withdraw(self,amount):
#         if(self.balance < amount) :
#             print("Insufficient Funds available !!!")
#         else:
#             print("Withdrawed: ",amount)
#             self.balance = self.balance - amount
#             return self.balance

#     def display(self):
#         print("Account Holder: ",self.account_holder)
#         print("Balance: ",self.balance)

# bankAcc = BankAccount("Roshen Perera", 0)
# print("Balance after Deposited: ",bankAcc.deposit(5000))
# print("Balance after Withdrawed: ",bankAcc.withdraw(4000))
# bankAcc.display()

# Inheritance in Python
# Inheritance is a way of creating a new class for using details of an existing class without modifying it. The newly formed class is a derived class (or child class). Similarly

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def display(self):
#         pass

# class Dog(Animal):
#     def speak(self):
#         print(self.name, "says Woof")

# class Cat(Animal):
#     def __init__(self, name):
#         super().__init__(name)

# dog = Dog("Dog")
# dog.speak()

# cat = Cat("Cat")
# cat.speak()

# Your task is creating library management system. 
# Base class is LibraryItem
# Attributes:
# 1. title(string) - to store the title of the item
# 2. author(string) - to store the name of the author
# 3. publication(int) - to store the publication year of the item

# Methods:
# 1. display_info() - to display the details of the item

# Derived class is Book is derived from LibraryItem
# Attributes:
# 1. genre(string) - to store the genre of the book
# 3. display_info() - to display the details of the book including the genre and ISBN number

# Methods:
# 1. ISBN(string) - to store the ISBN number of the book


# Derived class is Magazine is derived from LibraryItem
# Attributes:
# 1. issue(string) - to store the issue name of the magazine

# Methods:
# 1. display_info() - to display the details of the magazine including the issue name and issue number


#Task 
# Create instances of each class Book and Magazine classes with appropriate attributes and methods
# Call display_info() and print_info() methods of each instance to test inheritance and method overriding

# class LibraryItem:

#     def __init__(self, title, author, publication):
#         self.title = title
#         self.author = author
#         self.publication = publication

#     def display_info(self):
#         print("Title: ",self.title)
#         print("Author: ",self.author)
#         print("Publication: ",self.publication)

# class Book(LibraryItem):
#     def __init__(self, title, author, publication, genre, ISBN):
#         super().__init__(title, author, publication)
#         self.genre = genre
#         self.ISBN = ISBN
    
#     def display_info(self):
#         super().display_info()
#         print("Genre: ",self.genre)
#         print("ISBN: ",self.ISBN)

# class Magazine(LibraryItem):
#     def __init__(self, title, author, publication, issue):
#         super().__init__(title, author, publication)
#         self.issue = issue

#     def display_info(self):
#         super().display_info()
#         print("Issue: ",self.issue)

# book = Book("Linux > Windows", "Roshen Perera", 2021, "Programming", "123456")
# print("Book Details: ")
# book.display_info()
# print("")
# magazine = Magazine("Linux > Windows", "National Geographic", 2021, "June")
# print("Magazine Details: ")
# magazine.display_info()

# Polymorphism in Python

# Polymorphism is an ability (in OOP) to use a common interface for multiple forms (data types).
# It allows objects of different classes to be treated as objects of a common superclass.

# Encapuslation in Python
# By convention, attributes and methods with a single underscore are considered "protected", and those with a double underscore are considered "private".
# Protected attributes and methods should not be accessed from outside the class, but they can be accessed from a derived class.
# Private attributes and methods should not be accessed from outside the class, not even from a derived class.
# Public attributes and methods can be accessed from outside the class.

# class MyClass:
#     _test1 = "protected"
#     test2 = "private"

#     def __init(self):
#         print("Protected:",self._test1)
#         print("Private:",self.__test2)
    
# my_obj = MyClass()
# print(my_obj._test1) # Can access the protected attribute but not recommended
# print(my_obj.__test2) # AttributeError: 'MyClass' object has no attribute '__test2'

# Write a python program to create a class named "Quadratic Equation" that represents a quadratic equation of the form ax^2 + bx + c = 0. 
# The class should have the private attributes a, b, and c to store the coefficients of the quadratic equation.
# Create a constructor that takes the values of a, b, and c and initializes the attributes.
# A private method named __discriminant() that calculates the discriminant of the quadratic equation.
# A public method find_roots() that returns the roots of the quadratic equation using the formula x = (-b ± √(b^2 - 4ac)) / 2a
# 1. If d = 0 one real root
# 2. If d > 0 two distincts real roots
# 3. If d < 0 two complex roots

# class QuadraticEquation:
#     def __init__(self, a, b, c):
#         self.__a = a
#         self.__b = b
#         self.__c = c

#     def __discriminant(self):
#         return self.__b ** 2 - 4 * self.__a * self.__c

#     def find_roots(self):
#         D = self.__discriminant()
#         if D > 0 :
#             root_1 = (-self.__b + D ** 0.5) / (2 * self.__a)
#             root_2 = (-self.__b - D ** 0.5) / (2 * self.__a)
#             return root_1, root_2, "Two distinct real roots"
#         elif D == 0:
#             root = -self.__b / (2 * self.__a)
#             return root, "One real root"
#         else:
#             real = -self.__b / (2 * self.__a)
#             img = D ** 0.5 / (2 * self.__a)
#             return real, img, "Two complex roots"

# quadratic = QuadraticEquation(1, 5, 6)
# print(quadratic.find_roots())