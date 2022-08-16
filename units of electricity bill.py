# charge 
# first 100 units-no charge
# next 100 units-Rs.5/unit
# after 200 units-Rs.10/unit
units=int(input("enter the units:"))
if units<=100:
    print("no charges")
elif units>100 and units<=200:
    print("total:",(units-100)*5)
elif units>200:
    print("total:",(units-200)*10)
else:
    print("invalid input")

