'''
Write a program to find the smallest monthly payment to the cent such that we
can pay off the debt within a year.
'''

balance = 320000
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate / 12
minimum = balance / 12
maximum = (balance * (1 + monthlyInterestRate) ** 12) / 12
guess = (minimum + maximum) / 2
remainder = balance
epsilon = 0.01

while (remainder >= epsilon):
    guess = (minimum + maximum) / 2

    for i in range(1, 13):
        newBalance = remainder - guess
        monthlyInterest = (annualInterestRate / 12) * newBalance
        remainder = newBalance + monthlyInterest

    if (remainder < 0):
        maximum = guess
        remainder = balance

    elif (remainder > epsilon):
        minimum = guess
        remainder = balance

print('Lowest Payment: ' + str(round(guess, 2)))
