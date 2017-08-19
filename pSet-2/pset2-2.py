# pset 2-2 paying debt off in a year

month = 12
monthlyRate = annualInterestRate / 12
monthlyPayment = 10
unpaidBalance = balance

while month > 0 and unpaidBalance > 0:
    unpaidBalance = unpaidBalance - monthlyPayment
    interest = unpaidBalance * monthlyRate
    unpaidBalance = interest + unpaidBalance
    month -= 1
    if unpaidBalance <= 0:
        print(round(monthlyPayment, 2))
        break
    elif month == 0:
        unpaidBalance = balance
        monthlyPayment = monthlyPayment + 10
        month = 12    
