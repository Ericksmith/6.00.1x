month = 12
monthlyRate = annualInterestRate / 12

while month > 0:
    minMonthly = monthlyPaymentRate * balance
    balance = balance - minMonthly
    interest = balance * monthlyRate
    balance = interest + balance
    month -= 1
else:
    print(round(balance, 2))        
