month_name=input("enter the month:")
if month_name in("january","march","may","july","august","october","december"):
    print(month_name,":31days")
elif month_name in("april","june","september","november"):
    print(month_name,"30days")
elif month_name=="february":
    print(month_name,":28/29days")
else:
    print("invalid month")
    