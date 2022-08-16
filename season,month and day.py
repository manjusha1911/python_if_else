month=input("enter the number:")
day=int(input("enter the number:"))
if month in("march,april,may,tune"):
    if day>=1 and day<=31:
        print("summer")
    else:
        print("not summer")
elif month in("november,december,january,february"):
    if day>=1 and day<=31:
        print("winter")
    else:
        print("not winter")
elif month in("july,august,october,september"):
    if day>=1 and day<=31:
        print("monsoon")
    else:
        print("not monsoon")
else:
    print("no")