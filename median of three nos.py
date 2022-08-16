a=int(input("enter the number:"))
b=int(input("enter the number:"))
c=int(input("enter the number:"))
if a>b and a<c:
    print(a,"s is median")
elif b>a and b<c:
    print(b,"b is median")
elif c>a and c<b:
    print(c,"c is median")
else:
    print("all are equal")