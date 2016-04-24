TotalPaid = 0
for i in range(1,13):
    print 'Month: %d' %(i)
    Y = monthlyPaymentRate*balance
    TotalPaid = TotalPaid + Y
    print 'Minimum monthly payment: %.2f' % round(Y,4)
    X=balance-Y
    Z=(annualInterestRate/12)*X
    W = X+Z
    balance = W
    print 'Remaining Balance: %.2f' % round(W,4)

print 'TotalPaid: %.2f' % round(TotalPaid,4)
print 'Remaining Balance: %.2f' % round(W,4)

