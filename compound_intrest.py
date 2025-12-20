principal=float(input("enter the principal"))
rate=float(input("enter the rate"))
time=float(input("enter the time"))
amount=principal*(1+rate/100)**time
ci=amount-principal
print("copound intrest is",ci)