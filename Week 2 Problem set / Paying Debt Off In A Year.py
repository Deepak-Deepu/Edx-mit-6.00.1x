air=(annualInterestRate)/12
bal=balance
minipay=0
while bal>0:
        minipay += 10
        bal=balance
        for i in range(12):
                unpaidbal=bal-minipay
                bal=unpaidbal+unpaidbal*air


print "Lowest payment"+str(minipay)
                                            
