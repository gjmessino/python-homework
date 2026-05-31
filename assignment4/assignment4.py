import pandas as pd

# Task 1: Introduction to Pandas - Creating and Manipulating DataFrames
data = {'Name': ['Alice', 'Bob', 'Charlie'],
           'Age': [25, 30, 35],
           'City': ['New York', 'Los Angeles', 'Chicago']}

task1_data_frame = pd.DataFrame(data)
task1_with_salary = task1_data_frame.copy()
print(task1_data_frame)

task1_with_salary['Salary'] = [70000, 80000, 90000]
print(task1_with_salary)

task1_older = task1_with_salary.copy()
task1_older['Age'] +=1
print(task1_older)

task1_older.to_csv('employees.csv', index=False)

# Task 2: Loading Data from CSV and JSON
task2_employees = pd.read_csv('employees.csv')
print(task2_employees)

task2_data = ({'Name' : ['Eve', 'Frank'],
               'Age' : ['28', '40'],
               'City' : ['Miami', 'Seattle'],
               'Salary' : ['60000', '95000']})
task2_data['Age'] = pd.to_numeric(task2_data['Age'], errors='coerce')
json_employees = pd.DataFrame(task2_data)
json_employees.to_json('additional_employees.json', index = False)

more_employees = pd.concat ([task2_employees, json_employees], ignore_index=True)
print(more_employees)

# Task 3: Data Inspection - Using Head, Tail, and Info Methods

more_employees.head()
first_three = more_employees.iloc[0:3]
print(first_three)

print(more_employees.tail())

last_two = more_employees.iloc[3:]
print(last_two)

employee_shape = more_employees.shape
print(employee_shape)

more_employees.info()

# Task 4: Data Cleaning
dirty_data = pd.read_csv('assignment4/dirty_data.csv')
print(dirty_data.head())
clean_data = dirty_data.copy()
print(clean_data.tail())

clean_data = clean_data.drop_duplicates()
print(clean_data)

clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')
clean_data.info()

clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors='coerce')
print(clean_data['Salary'])

clean_data['Age'] = clean_data['Age'].fillna(clean_data['Age'].mean())
clean_data['Salary'] = clean_data['Salary'].fillna(clean_data['Salary'].median())

clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], errors='coerce')

clean_data['Name'] = clean_data['Name'].str.strip()
clean_data['Name'] = clean_data['Name'].str.upper()
clean_data['Department'] = clean_data['Department'].str.strip()
clean_data['Department'] = clean_data['Department'].str.upper()

print(clean_data)