import random
import csv

names = ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Fay', 'George', 'Hannah', 'Ian', 'Jack']
salaries = [random.randint(40000, 100000) for _ in range(20)]

with open('employee_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Employee Name", "Salary"])
    for i in range(20):
        writer.writerow([names[i % len(names)], salaries[i]])
