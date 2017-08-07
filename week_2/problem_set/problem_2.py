'''
Now write a program that calculates the minimum fixed monthly payment needed in
order pay off a credit card balance within 12 months. By a fixed monthly
payment, we mean a single number which does not change each month, but instead
is a constant amount that will be paid each month.
'''

balance = 3329
annualInterestRate = 0.2

monthlyPayment = 0
monthlyInterestRate = annualInterestRate / 12
newBalance = balance
month = 0

while newBalance > 0:
    monthlyPayment = monthlyPayment + 10
    newBalance = balance

    for month in range(1, 13):
        newBalance = newBalance - monthlyPayment
        newBalance = newBalance + (monthlyInterestRate * newBalance)
        month = month + 1

print('Lowest Payment: ' + str(monthlyPayment))
