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
import csv

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