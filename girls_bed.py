girls=int(input("enter the number of girls:"))
beds=int(input("enter the number of beds:"))
if girls>beds:
    print(girls-beds,"beds shortage")
elif girls<beds:
    print(beds-girls,"beds left")
else:
    print("room full")