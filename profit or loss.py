sp=int(input("enter the selling price:"))
lp=int(input("enter the landing price:"))
if sp>lp:
    print("profit=",sp-lp)
elif sp<lp:
    print("loss=",sp-lp)
else:
    print("no prifit no loss")