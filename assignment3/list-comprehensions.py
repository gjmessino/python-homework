import csv

with open('csv/employees.csv', 'r') as file:
    reader = csv.reader(file)
    first_row = next(reader)
    first_last = [row[1] + " " + row[2] for row in reader]
print(first_last)
e_names = [name for name in first_last if "e" in name]
print(e_names)