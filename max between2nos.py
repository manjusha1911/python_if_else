# a=int(input("enter the number:"))
# b=int(input("enter the number:"))
# c=int(input("enter the number:"))
# d=int(input("enter the number:"))
a=20
b=100
c=40
d=10
if a>b and a>c and a>d:
    print(a,"a is maximum")
elif b>a and b>c and b>d:
    print(b,"b is maximum")
elif c>a and c>b and c>d:
    print(c,"c is maximum")
else:
    print(d,"d is maximum")