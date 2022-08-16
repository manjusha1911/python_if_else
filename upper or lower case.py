x=input("enter the number:")
if x>="A" and x<="Z":
    print(x,"x is an upper")
elif x>="a" and x<="z":
    print(x,"x is a lower case")
elif x>="A" or x<="Z" and x>="a" and x<="z":
    print("upper and lower")
else:
    print("enter valid input")