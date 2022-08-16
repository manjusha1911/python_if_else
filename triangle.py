# triangle =180

# x=int(input("enter the number:"))
# y=int(input("enter the number:"))
# z=int(input("enter the number:"))
# if x+y+z==180:
#     print("triangle")
# else:
#     print("not a triangle")

#equilateral triangle:
#all sides are eual is called equilateral

# a=int(input("enter the number:"))
# b=int(input("enter the number:"))
# c=int(input("enter the number:"))
# if a==b and b==c and c==a:
#     print("equilateral")
# else:
#     print("not equilateral")

# Isosceles triangle:
# two sides are equal  

# a=int(input("enter the number:"))
# b=int(input("enter the number:"))
# c=int(input("enter the number:"))
# if a==b!=c or b==c!=a or c==a!=a:
#     print("Isosceles")
# else:
#     print("not Isosceles")

# scelene
# all triangle are unequal
# a=int(input("enter the number:"))
# b=int(input("enter the number:"))
# c=int(input("enter the number:"))
# if a!=b and b!=c and c!=a:
#     print("scelene")
# else:
#     print("not scelene")


a=int(input("enter the number:"))
b=int(input("enter the number:"))
c=int(input("enter the number:"))
if a==b!=c or b==c!=a or c==a!=a:
    print("Isosceles")
elif a==b and b==c and c==a:
    print("equilateral")
elif a!=b and b!=c and c!=a:
    print("scelene")
else:
    print("enter valid input")