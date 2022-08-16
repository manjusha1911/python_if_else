# electricity unit charges and calculate total electricity Billboard
# for first 50 units Rs. 0.50/unit
# for next 100 units Rs. 0.75/units
# for next 150 units Rs. 1.20/units
# for next 250 units Rs. 1.20/units
# an aditional subcharge of 20% is added to the bill
units=int(input("enter the number:"))
total=subcharge=amount=0
if units<=50:
    amount=units*0.50
    subchange=amount*20/100
    print("total bill:",amount+subcharge)
elif units<=100:
    amount=units*0.75
    subchange=amount*20/100
    print("total bill:",amount+subcharge)
elif units<=150:
    amount=units*1.20
    subcharge=amount*20/100
    print("total bill:",amount+subcharge)
else:
    amount=units*1.20
    subcharge=amount*20/100
    print("total bill:",amount+subcharge)

