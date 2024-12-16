# EXERCISE 03
# You are tasked with a creating a python program to manage a companies employee details stored in csv file. 
# The program should read the employee details from the csv file, filter the records based on the condition and write the filtered records to a new csv file.

# Input file: employee.csv contains the following fields: EmployeeID, Name, Department, Salary
# Output file: high_salary_employees.csv contains the highest paid employees. It should contain records of employees with a salary greater than 57000. The fields should be the same.

# Task 1: Read the employee details from the input file, use csv.reader to read employee.csv file and display all the records on the console.
# Task 2: Filter the records identify the employees with a salary greater than 57000.
# Task 3: Write the filtered records using csv.writer to create a new csv file named high_salary_employees.csv.

# csv_file_path = "DAY 06\output.csv"

# data = [ 
#     {"Name": "John", "Age": 19, "City": "Avissawella"},
#     {"Name": "Jane", "Age": 20, "City": "Colombo"},
#     {"Name": "Doe", "Age": 21, "City": "Kandy"}
# ]

# import csv

# csv_file_path = "DAY 06\Exercise 03\employee.csv"

# print("Employee Details")
# with open(csv_file_path, "r", newline="") as csv_file:
#     # Create a CSV reader object
#     employees = csv.DictReader(csv_file)
#     for employee in employees:
#         print(employee)

# filtered_employees = []

# print("\nEmployee names with salary more than 57000")
# with open(csv_file_path, "r", newline="") as csv_file:
#     # Create a CSV reader object
#     employees = csv.DictReader(csv_file)
#     for employee in employees:
#         if(int(employee["Salary"]) > 57000):
#             print(employee["Name"])
#             filtered_employees.append(employee)

# print(filtered_employees)

# fieldnames = ["EmployeeID","Name","Age","Salary"]

# new_csv = "DAY 06\Exercise 03\high_salary_employees.csv"

# with open(new_csv, "w", newline="") as csv_file:
#     employees = csv.DictWriter(csv_file, fieldnames=fieldnames)
#     employees.writeheader()
#     employees.writerow(filtered_employees)

# with open(new_csv, "w", newline="") as csv_file:
#     employee = csv.DictWriter(new_csv)
#     employee.writerow(new_csv)


    # Create a CSV writer object
#     csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#     # Write the header (column names) to the CSV file
#     csv_writer.writeheader()
#     # Write the data to the CSV file
#     for row in data:
#         csv_writer.writerow(row)
#         print(row, type(row))
