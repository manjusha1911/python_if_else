# a=3
# b=10
# if a>b:
#     print(a,"a is maximum")
# else:
#     print(b,"b is maximum")
x=int(input("enter the number:"))
y=int(input("enter the number:"))
z=int(input("enter the number:"))
if x>y and x>z:
    print(x,"X is maximum number")
elif y>x and y>z:
    print(y," Y is maximum")
else:
    print(z,"Z is maximum")
