# Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria : 
#  Cost price (in Rs)           Tax
#       a)  > 100000                    15 %
#       b)  > 50000 and <= 100000       10%
#        c) <= 50000                     5%
a=int(input("enter the amount:"))
cost=a
if a>100000:
    tax=cost*15/100
    print("tax:",tax)
elif a>50000 and a<=100000:
    tax=cost*10/100
    print("tax",tax)
elif a<=50000:
    tax=cost*5/100
    print("tax:",tax)
else:
    print("no")