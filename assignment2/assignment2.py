import os
import custom_module
import csv
from datetime import datetime

# Task 1: Diary
def diary():
    try:
        with open('diary.txt', 'a') as file:
            first = input("What happened today? ")
            writer = csv.writer(file)
            writer.writerow(first)
            not_done = True
            while not_done:
                new_line = input("What else? ")
                writer.writerow(new_line)
                if new_line == "done for now":
                    writer.writerow(new_line)
                    not_done = False
    except Exception as e:
        print(f"An exception has occured. {e}")
        return
diary()

# Task 2: Read a CSV File
def read_employees():
    try:
        my_dict = {}
        my_list = []
        with open('csv/employees.csv', 'r') as file:
            reader = csv.reader(file)
            my_dict['fields'] = next(reader)
            for row in reader:
                my_list.append(row)
            my_dict['rows'] = my_list
        return my_dict
    except Exception as e:
        print(f"An exception has occured. {e}")
        return
employees = read_employees()

# Task 3: Find the Column Index
def column_index(col):
    try:
        return employees["fields"].index(col)
    except Exception as e:
        print(f"An exception has occured. {e}")
        return
employee_id_column = column_index('employee_id')

# Task 4: Find the Employee First Name
def first_name(num_row):
    col_ind = column_index('first_name')
    row = employees['rows'][num_row]
    return row[col_ind]

# Task 5: Find the Employee: a Function in a Function
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches = list(filter(employee_match, employees["rows"]))
    return matches

#Task 6: Find the Employee with a Lambda
def employee_find_2(employee_id):
   matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
   return matches

#Task 7: Sort the Rows by last_name Using a Lambda
def sort_by_last_name():
    last_name_column = column_index('last_name')
    employees["rows"].sort(key = lambda row : row[last_name_column])
    return employees['rows']

#Task 8: Create a dict for an Employee
def employee_dict(row):
    key_list = employees['fields']
    val_list = []
    for item in row:
        val_list.append(item)
    my_zip = zip(key_list, val_list)
    my_dict = dict(my_zip)
    del my_dict['employee_id']
    return my_dict

# Task 9: A dict of dicts, for All Employees
def all_employees_dict():
    emp_dicts = {}
    ind = column_index('employee_id')
    for item in employees['rows']:
        id = item[ind]
        emp_dicts[id] = tuple(employee_dict(employees['rows'][item]))
    return emp_dicts

# Task 10: Use the os Module
def get_this_value():
    val = os.getenv('THISVALUE')
    return val

# Task 11: Creating Your Own Module
def set_that_secret(secret):
    sec = custom_module.set_secret(secret)
    print(sec)

# Task 12: Read minutes1.csv and minutes2.csv
def read_minutes():
    def file_read(minutes):
        with open (minutes, 'r') as file:
            mins = {}
            min_list = []
            reader = csv.reader(file)
            mins['fields'] = next(reader)
            for row in reader:
                min_list.append(tuple(row))
            mins['rows'] = min_list
        return mins
    min1 = file_read('csv/minutes1.csv')
    min2 = file_read('csv/minutes2.csv')
    return min1, min2

# Task 13: Create minutes_set
def create_minutes_set():
    a,b = read_minutes()
    def make_set(my_dict, my_set = set()):
        for row in my_dict:
            my_set.add(row)
        return my_set
    aset = make_set(a['rows'])
    bset = make_set(b['rows'])
    combo = aset.union(bset)
    return combo
minutes_set = create_minutes_set()

# Task 14: Convert to datetime
def create_minutes_list():
    my_list = list(map((lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y"))), (minutes_set)))
    return my_list
minutes_list = create_minutes_list()

# Task 15: Write Out Sorted List
def write_sorted_list():
    sorted_list = sorted(minutes_list, key = lambda x : x[1])
    my_list = list(map(( lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y"))), (sorted_list)))
    with open('./minutes.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Date'])
        for line in my_list:
            writer.writerow(line)
write_sorted_list()