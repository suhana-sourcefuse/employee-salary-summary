import pandas as pd


df = pd.read_csv('employee_data.csv')


total_employees = len(df)
average_salary = df['Salary'].mean()


output = pd.DataFrame({
    "Number of Employees": [total_employees],
    "Average Salary": [average_salary]
})


output.to_csv('output.csv', index=False)

#updating
