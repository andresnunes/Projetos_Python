'''
Exercise 1: Rewrite your pay computation to give the employee 1.5
times the hourly rate for hours worked above 40 hours.
Enter Hours: 45
Enter Rate: 10
Pay: 475.0 (acho q é 675)
'''
hours = float(input("Enter Hours : "))
rate = float(input("Enter Rate : "))

pay = hours * rate

if hours > 40:
    pay = pay*1.5

print("Pay : ",round(pay,2))
