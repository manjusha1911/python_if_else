x=input("enter the alphabet:")
if (x>="a" and x<="z") or (x>="A" and x<="Z"):
    print("x is an alphabet")
elif x>="0" and x<="9":
    print("x is a digit")
else:
    print("x is a special character")