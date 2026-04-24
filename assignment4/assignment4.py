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
