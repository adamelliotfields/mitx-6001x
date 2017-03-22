'''
For each month, calculate statements on the monthly payment and remaining
balance. At the end of 12 months, print out the remaining balance. Be sure to
print out no more than two decimal digits of accuracy.
'''

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthlyInterestRate = annualInterestRate / 12
monthlyPayment = monthlyPaymentRate * balance
newBalance = (balance - monthlyPayment) * (1 + monthlyInterestRate)

for month in range(1, 13):
    monthlyPayment = monthlyPaymentRate * balance
    balance = (balance - monthlyPayment) * (1 + monthlyInterestRate)

print('Remaining balance: ' % (round(monthlyPayment, 2), round(balance, 2)))
