def computepay():
    hrs=input()
    h=float(hrs)
    rate=input()
    r=float(rate)
    if h<=40:
        pay=h*r
    elif h>40:
         d=h-35
    pay=(40*r)+(d*(r*1.5))
    print('Pay',pay)
    return pay
computepay()
print('Your final pay')