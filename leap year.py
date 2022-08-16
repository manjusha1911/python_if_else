year=int(input("enter the number:"))
if year%100==0:
    if year%400==0:
        print(year,"leap year")   
else:
    if year%4==0:
        print(year,"leap year")
    else:
        print(year,"not a leap year")