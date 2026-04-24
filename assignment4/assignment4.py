import pandas as pd
# Task 1: Introduction to Pandas - Creating and Manipulating DataFrames
data = {'Name': ['Alice', 'Bob', 'Charlie'],
           'Age': [25, 30, 35],
           'City': ['New York', 'Los Angeles', 'Chicago']}

task1_data_frame = pd.DataFrame(data)
task1_with_salary = task1_data_frame.copy()
print('Original Data')
print(task1_data_frame)

task1_with_salary['Salary'] = [70000, 80000, 90000]
print('Add Salary')
print(task1_with_salary)

task1_older = task1_with_salary.copy()
task1_older['Age'] +=1
print('Incriment Age')
print(task1_older)

task1_older.to_csv('employees.csv', index=False)

# Task 2: Loading Data from CSV and JSON
task2_employees = pd.read_csv('employees.csv')
print('Reprinting Data from Task 1')
print(task2_employees)

task2_data = ({'Name' : ['Eve', 'Frank'],
               'Age' : ['28', '40'],
               'City' : ['Miami', 'Seatle'],
               'Salary' : ['60000', '95000']})
json_employees = pd.DataFrame(task2_data)
json_employees.to_json('additional_employees.json', index = False)

more_employees = pd.concat ([task2_employees, json_employees], ignore_index=True)
print('Task 2 Data')
print(more_employees)

# Task 3: Data Inspection - Using Head, Tail, and Info Methods
print('Head')
more_employees.head()

first_three = more_employees.iloc[0:3]
print('First Three')
print(first_three)

print('Tail')
print(more_employees.tail())

print('Last Two')
last_two = more_employees.iloc[3:]
print(last_two)

employee_shape = more_employees.shape
print('Shape')
print(employee_shape)

print('Info')
more_employees.info()