#This calculates the monthly payments of loan.

loanamount = input("Write your loan amount \n " )
interestrate = input("Enter your interest rate here \n ")
payments = input("Enter you number of payments (in year)  \n")

#Converting string into float.

loanamount = float(loanamount)
interestrate = float(interestrate)
payments = float(payments)

#Converting interest rate into amount to  and  years into total number of payments.

interest = interestrate / 100 / 12
noofpayments = payments * 12
 


#M = L[i(1+i)n] / [(1+i)n-1]
# M = monthly payment, L = Loanamount, i = interest rate and n = no of payments 

Monthlypayment = loanamount * interest * (1 + interest) ** noofpayments / (( 1 + interest ) ** noofpayments - 1 )
 
print(Monthlypayment)