# Write a program to accept two numbers and mathematical operators and perform operation accordingly.
# Like:
# Enter First Number: 7
# Enter Second Number : 9
# Enter operator : +
# Your Answer is : 16
a=int(input("enter the number:"))
b=int(input("enter the number:"))
c=input("enter the operator:")
if a>0 and b>0:
    if c=="+":
        print(a+b) 
    if c=="-":
        print(a-b)
    if c=="*":
        print(a*b)
    if c=="%":
        print(a%b)
else:
    print("enter vaild input")
