## What is a Python Library? Why do we use it?
# In Python, libraries are collections of pre-writtern code and modules that provide a wide range of functionality to simplify the development of programs. 
# These libraries contain functions, classes, and methods that can be imported and used in your Python programs, reducing the amount of code you need to write and speeding up the development process.

## Module vs Library

# A module is a single file that contains Python code. 
# It can define functions, classes, and variables, and can be imported and used in other Python programs.
# Modules are used to organize code and make it easier to manage and reuse.

# A library is a collection of modules that provide a specific set of functionality.
# Libraries can contain multiple modules, each of which provides different features and capabilities.
# Libraries are used to extend the functionality of Python and provide additional tools and resources for developers.

## Open source libraries
# Open source libraries are libraries that are freely available for anyone to use, modify, and distribute.
# These libraries are typically developed by a community of developers who contribute code and collaborate on projects.
# Open source libraries are often hosted on platforms like GitHub, where users can access the source code, report issues, and contribute to the development of the library.

## Selecting relavant libraries
# When selecting libraries for your Python projects, it's important to consider the requirements of your project and the functionality you need.
# Some factors to consider when choosing libraries include:
# The features and capabilities provided by the library.
# The ease of use and documentation of the library.
# The performance and efficiency of the library.
# The community and support around the library.
# The licensing and compatibility of the library with your project.

## Popular Python Libraries
# There are thousands of Python libraries available, covering a wide range of topics and domains.
# Some of the most popular Python libraries include:
# NumPy: A library for numerical computing that provides support for arrays, matrices, and mathematical functions.
# Pandas: A library for data manipulation and analysis that provides data structures like DataFrames and Series.
# Matplotlib: A library for creating visualizations and plots, including line charts, bar charts, and scatter plots.
# Requests: A library for making HTTP requests and working with APIs.
# TensorFlow: A library for machine learning and deep learning that provides tools for building and training neural networks.
# Django: A web framework for building web applications and APIs.
# Flask: A lightweight web framework for building web applications and APIs.
# Scikit-learn: A library for machine learning that provides tools for classification, regression, clustering, and more.
# BeautifulSoup: A library for parsing HTML and XML documents, used for web scraping and data extraction.
# OpenCV: A library for computer vision and image processing that provides tools for working with images and videos.
# Pygame: A library for game development that provides tools for creating 2D games and multimedia applications.
# Pytorch: A library for machine learning and deep learning that provides tools for building and training neural networks.

## NumPy Library
# NumPy is a popular Python library for numerical computing that provides support for arrays, matrices, and mathematical functions.
# NumPy, which stands for Numerical Python, is a fundamental open-source library in python thar provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays.    
# NumPy is widely used in scientific computing, data analysis, and machine learning applications, and is an essential tool for working with numerical data in Python.

# Array creation:
# You can create an array from a regular Python list or tuple using the array function.
import numpy as np

# a = np.array([1, 2, 3])
# print(a)
# print(type(a))

# # Creating NumPy arrays

# array1 = np.array([1, 2, 3, 4, 5])
# array2 = np.array([6, 7, 8, 9, 10])

# # Adding two arrays
# print(array1+array2)

# # Subtracting two arrays
# print(array1-array2)

# # Multiplying two arrays
# print(array1*array2)

# # Dividing two arrays
# print(array1/array2)

# # The length of the array should be the same, otherwise it will throw an error.
# #  array3 = np.array([1, 2, 3, 4])
# #  print(array1+array3) # ValueError: operands could not be broadcast together with shapes (5,) (4,)

# # Square root of an array
# print(np.sqrt(array1))

# # Summation of an array
# print(np.sum(array1))

# # Mean of an array
# print(np.mean(array1))

# # Maximum value of an array
# print(np.max(array1))

# # Minimum value of an array
# print(np.min(array1))

# Multidimensional arrays
# You can create multidimensional arrays by passing a list of lists to the array function.
# array2d = np.array([[1, 2, 3], [4, 5, 6]]) # 3x2 array (3 rows, 2 columns)
# print(array2d)

# array2d1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # 3x3 array (3 rows, 3 columns)
# print(array2d1)

# array3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]) # 2x2x3 array (2 matrices, 2 rows, 3 columns) #Outermost array is the number of matrices
# print(array3d)

# print(array2d.shape) # (3, 3)
# print(array3d.shape) # (2, 2, 3)
# print(array2d.size) # 9

# Shape
# The shape attribute returns a tuple containing the dimensions of the array. 

# Size
# The size attribute returns the total number of elements in the array.

# dType
# The dtype attribute returns the data type of the elements in the array.

# arrayD = np.array([1, 2, 3, 4, 5])
# print(arrayD.dtype) # int64

# arrayD1 = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
# print(arrayD1.dtype) # float64

# # You can also specify the data type when creating an array by passing the dtype argument to the array function.
# arrayD2 = np.array([1, 2, 3, 4, 5], dtype='float64')
# print(arrayD2.dtype) # float64

# arrayD3 = np.array([True, False, True, False])
# print(arrayD3.dtype) # bool

# # ndim
# # The ndim attribute returns the number of dimensions of the array. 
# arrayNdim = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(arrayNdim.ndim) # 2

# arrayNdim1 = np.array([1, 2, 3, 4, 5])
# print(arrayNdim1.ndim) # 1

# arrayNdim2 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(arrayNdim2.ndim) # 3

# NumPy Array Indexing
# You can access elements of a NumPy array using indexing.
# Indexing starts at 0, so the first element of an array has an index of 0, the second element has an index of 1, and so on.

# arrayIndex = np.array([1, 2, 3, 4, 5])
# print(arrayIndex[0]) # 1

# # You can also use negative indices to access elements from the end of the array.       
# # print(arrayIndex[-1]) # 5

# arrayIndex2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(arrayIndex2[0, 0]) # 1

# arrayIndex3 = np.array([[[1, 2, 3], [4, 5, 6]],[[7, 8, 9], []]])

# 1. create a 2d numpy array which has dimensions 4 x 5 which contains the numbers 1 to 20.
# Perform the following on the array:

# Add 10 to every element
# Multiply every element by 2
# Calculate the square of each element

# exArray = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]])
# print(exArray.shape)

# print(exArray+10)

# print(exArray*2)

# print(exArray**2)

# Without using any loops, you can perform operations on the entire array at once, which is much faster and more efficient than using loops to iterate over each element.

# Boelean Indexing
# You can use boolean indexing to filter elements of an array based on a condition.
# Boolean indexing returns a new array containing only the elements that satisfy the condition.

# arrayBool = np.array([1, 2, 3, 4, 5])
# print(arrayBool[arrayBool>2]) # [3, 4, 5] # It will return the elements that are greater than 2.
# print(arrayBool>2) # [False False True True True] # It will return the boolean values based on the condition.

# condition = arrayBool>2
# filtered = arrayBool[condition]
# print(filtered)

# Boolean Indexing in NumPy

## Combining mutliple conditions
# You can combine multiple conditions using logical operators like & (and), | (or), and ~ (not).

# arrayBool1 = np.array([1, 2, 3, 4, 5])
# condition1 = (arrayBool1>2) & (arrayBool1<5)
# filtered1 = arrayBool1[condition1]
# print(filtered1) # [3, 4]

# Array Initialization - np.zeros(), np.ones(), np.full(), np.eye()

# np.zeros() - Create an array of zeros with the specified shape.
# np.ones() - Create an array of ones with the specified shape.
# np.full() - Create an array with the specified shape and fill it with the specified value.
# np.eye() - Create an identity matrix with the specified size.

#np.zeros()
# Initialize an array of zeros with the specified shape.
# Parameters:
# shape(required): The dimensions of the array. Can be an integer or a tuple of integers.
# dtype(optional): The data type of the array elements such as int, float, etc. Default is float.
# syntax: np.zeros(shape, dtype=float, order='C')

# arrayInit = np.zeros((5))
# print(arrayInit) # [0. 0. 0. 0. 0.]

# arrayInit1 = np.zeros((2, 3))
# print(arrayInit1) # 

#np.full()
# Initialize an array with the specified shape and fill it with the specified value.
# Parameters:
# shape(required): The dimensions of the array. Can be an integer or a tuple of integers.
# fill_value(required): The value to fill the array with.
# dtype(optional): The data type of the array elements such as int, float, etc. Default is float.
# syntax: np.full(shape, fill_value, dtype=None, order='C')

# arrayInit2 = np.full((2, 3), 5)
# print(arrayInit2) # [[5 5 5] [5 5 5]]

# arrayInit3 = np.full(4, 10)
# print(arrayInit3) # [10 10 10 10]

#np.empty()
# Initialize an array with random values.
# This function does not initialize the array elements to zero or any other value.
# Instead, it returns an array with uninitialized values, which may contain random data.
# This method is faster than np.zeros() as it does not initialize the array elements.
# The values are fetched from the garbage memory.
# Parameters:
# shape(required): The dimensions of the array. Can be an integer or a tuple of integers.
# dtype(optional): The data type of the array elements such as int, float, etc. Default is float.
# syntax: np.empty(shape, dtype=float, order='C')

# arrayInit4 = np.empty((2, 3))
# print(arrayInit4)

# #1. Create a 1D numpy array with values from 1 to 20. Use boolean indexing to extract only the even numbers from the array.

# exArray1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
# condtion = exArray1%2 == 0
# filtered = exArray1[condtion]
# print(filtered)


# #2. Create a 1D numpy array with elements 10, 20, 30, 40, 50. Use boolean indexing to extract only the elements greater than the mean of the array.

# exArray2 = np.array([10, 20, 30, 40, 50])
# condtion2 = exArray2 > np.mean(exArray2)
# filtered2 = exArray2[condtion2]
# print(filtered2)

# Pandas Libray

# Pandas is a popular Python library for data manipulation and analysis that provides data structures like DataFrames and Series
# It is widely used in data science, machine learning, and other domains for working with structured data.

# DataFrames

# A DataFrame in Pandas is like a table in Excel or a database: it's a two-dimensional data structure with rows and columns.
# Each column can have a diffent data type, such as integer, float, string, etc.
# A DataFrame is a 2-dimensional labeled data structure with columns of potentially different types.
# It is similar to a spreadsheet or SQL table, where each column represents a different variable or feature, and each row represents a different observation or data point.
# DataFrames are commonly used to store and manipulate tabular data, such as data from CSV files, databases, or other sources.

# Creating DataFrames
import pandas as pd

# data = {
#         'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
#         'Age': [25, 30, 35, 40, 45],
#         'City': ['Avissawella', 'Eheliyagoda', 'Getahetta', 'Colombo', 'Rathnapura']
#         }

# df = pd.DataFrame(data)
# print(df)
# print(type(df))

# Dataframes put index to each row by default. You can also specify the index by passing the index argument to the DataFrame function.
# df1 = pd.DataFrame(data, index=['A', 'B', 'C', 'D', 'E'])

# Accessing DataFrames
# You can access columns of a DataFrame using the column name.
# You can access rows of a DataFrame using the row index.

# print(df.loc[1,"Name"]) # Bob # loc is used to access the rows and columns by their labels.
# print(df.iloc[1, 0]) # Bob # iloc is used to access the rows and columns by their integer index.

# print(df['Name'])

# Locating Rows
# You can locate rows in a DataFrame using the loc[] method.
# print(df.loc[1]) # Accessing the row with index 1

# print(df.loc[[0, 1]]) # Accessing the rows with index 0 and 1. Multiple rows can be accessed by passing a list of row indices.
# print(df.loc[1:3]) # Accessing the rows with index 1 to 3. Slicing can also be used to access multiple rows.

# Add a list of names to give each row a name:

# data = {
#     "Calories": [450, 300, 250],
#     "Duration": [60, 30, 45]
# }

# df = pd.DataFrame(data, index=["Day1", "Day2", "Day3"])
# print(df) # Named Indexes

# print(df.loc["Day2"]) # Accessing the row with index "Day2"
# print(df.loc["Day1", "Day3"]) # Accessing the rows with index "Day1" and "Day3"

# Accessing Columns
# You can access columns of a DataFrame using the column name.
# You can access columns using the column name as an attribute of the DataFrame.
# You can also access columns using the column name as a key of the DataFrame.

# print(df[["Calories", "Duration"]]) # Accessing the "Calories" column. Multiple columns can be accessed by passing a list of column names.

# Useful Attributes and Methods
# DataFrame.shape: Returns the dimensions of the DataFrame as a tuple (rows, columns).

# df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
# print(df.shape) # (2, 2) 

# Useful Attributes: 

# DataFrame.columns
# Returns an Index object containing the column labels of the DataFrame.

# df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
# # print(df.columns) # Index(['A', 'B'], dtype='object')

# DataFrame.dtypes
# # print(df.dtypes)


# DataFrame.values
# print(df.values)
# # Output:
# # [[1 3]
# #  [2 4]]

# print(type(df.values))

# DataFrame.len()
# Returns the number of rows in the DataFrame.

# data = {
#     'Age': [25, 30, 35, 40, 45],
#     'Salary': [50000, 60000, 70000, 80000, 90000]
# }

# df = pd.DataFrame(data)
# print(len(df)) # 5

# Your a data analyst at a retail compony. The company has provide with the above table which contains sales data.
# Your task is analyze sales data by using python and pandas library. To answer the following questions:
# Calculate the total revenue generated by the company for each order.
# Add a new column to store the total revenue for each order.
# Identiy the best selling product.
# Find the product with highest total sales revenue.

# data = {
#     'Product': ['Laptop', 'Smartphone', 'Desk chair', 'Monitor', 'BookShelf'],
#     'Category': ['Electronics', 'Electronics', 'Furniture', 'Electronics', 'Furniture',],
#     'Quantity': [2, 5, 10, 4, 2],
#     'Price': [1000, 800, 150, 200, 300],
#     'Region':['North', 'South', 'East', 'West', 'North']}

# df = pd.DataFrame(data, index=[101, 102, 103, 104, 105])
# # print(df)

# df['Revenue'] = df["Quantity"]*df["Price"]
# # print(df)

# # maxRevenue = df.groupby('Name')['Quantity'].idxmax()
# print(df.idxmax())

# DataFrame.mean()
# Returns the mean of the values in the DataFrame.

data = {
    'Age': [25, 30, 35, 40, 45],
    'Salary': [50000, 60000, 70000, 80000, 90000]
}

df = pd.DataFrame(data)
# print(df.mean()) # Age      35.0 Salary    70000.0 dtype: float64

# DataFrame.sum()
# Returns the sum of the values in the DataFrame.

# print(df.sum()) # Age          175 Salary    350000 dtype: int64

# DataFrame.describe()
# Generates descriptive statistics for the DataFrame.

print(df.describe())