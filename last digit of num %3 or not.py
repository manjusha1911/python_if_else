# a=int(input("enter the number:"))
# if a>0 and a%3==0:
#     print(a%10)
#     if a%3==0:
#         print(a,"divisible by 3")
#     else:
#         print(a,"not divisible")
# else:
#     print("not divible")
a=int(input("enter the number:"))
if a>0:
    a=a%10
    if a%3==0:
        print("divisible")
    else:
        print("not divisible")
else:
    print("less than 0")
