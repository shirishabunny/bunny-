"""calculate the compound intrest.
:param principal:the intial amount of money (float or int).
:param rate:the annual intrest rate(flot or int).
:param time:the number of periods the money is invested for(flot or int).
:return: the compound intrest (flot).
""""
# convert rate from percentage to decimal
rate_decimal =rate/100
# calculate the compound intrest 
amount= principal*(1+rate_decimal)**Time
compound_intrest=amount-principal
return compound_intrest
#input values
principal=float(input("enter the principal amount:"))
rate=float(input("enter the annual intrest rate(in percentage):"))
time=float(input("enter the number period:"))
#calculate compound intrest 
intrest=
calculate_compund_interst(principal,rate,Time)
#output the result 
print(f"the compound intrest is:
      {intrest:.2f}")

      
