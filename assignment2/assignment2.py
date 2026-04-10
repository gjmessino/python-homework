#import os
import custom_module
import csv

# Task 1: Diary
def diary():
    try:
        with open('diary.txt', 'a') as file:
            file.append(input("What happened today?"))
            done = False
            while done == False:
                new_line = file.append(input("What else?"))
                if new_line == "done for now":
                    done == True
                    file.close()
    except Exception as e:
        print(f"An exception has occured. {e}")
        return

# Task 2: Read a CSV File
def read_employees():
    try:
        my_dict = {}
        my_list = []
        with open('../csv/employees.csv', 'r') as file:
            reader = csv.reader(file)
            my_dict['field'] = next(reader)
            for row in reader:
                my_list.append(row)
            my_dict['rows'] = my_list
        return my_dict
    except Exception as e:
        print(f"An exception has occured. {e}")
        return

employees = read_employees()
print(employees)

# Task 3: Find the Column Index
def column_index(first_name):
    employees = read_employees()
    try:
        return employees["fields"].index("first_name")
    except Exception as e:
        print(f"An exception has occured. {e}")
        return

# Task 4: Find the Employee First Name
#def first_name(num):

# Task 10: Use the os Module
#def get_this_value():

# Task 11: Creating Your Own Module
def set_that_secret(secret):
    sec = custom_module.set_secret(secret)
    print(sec)
    sec = custom_module.set_secret('AppleSauce')
    print(sec)

# Task 12: Read minutes1.csv and minutes2.csv
def read_minutes():
    minutes1 = make_dict('minutes1')
    minutes2 = make_dict('minutes2')
    return minutes1, minutes2
def make_dict(dict_name):
    my_list = []
    my_dict = {}
    with open ('../csv/{dict_name}.csv', r) as file:
        reader = csv.reader(file)
        my_dict['field'] = next(reader)
        for row in reader:
            my_list.append(row)
        my_dict['rows'] = my_list
        file.close()
    return my_dict
