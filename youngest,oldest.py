a=int(input("enter the age of A:"))
b=int(input("enter the age of B:"))
c=int(input("enter the age of C:"))
if a>b and a>c:
    print("a is oldest")
if a<b and a<c:
    print("a is youngest")
if b>a and b>c:
    print("b is oldest")
if b<a and b<c:
    print("b is youngest")
if c>a and c>b:
    print("c is oldest")
elif c<a and c<b:
    print("c is youngest")
else:
    print ("all are eual age")