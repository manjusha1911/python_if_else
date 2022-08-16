a=int(input("enter the amount:"))
if a>=1000:
    discount=a*10/100
    print("discount amount",a-discount)
else:
    print("no discount")