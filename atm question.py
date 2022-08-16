language=input("enter the language:")
current_balance=25000
if language=="english":
    print("welcome to hdfc")
    print("please insert your card")
    password=int(input("enter the pin"))
    pin=4040
    if pin==password:
        menu=input("select the option:")
        if menu=="b":
            if current_balance>0:
                print(current_balance)
            else:
                print("zero balance")
        elif menu=="w":
            withdrawal_amount=int(input("enter the amount"))
            if withdrawal_amount<=current_balance: 
                print("trasation successful",current_balance-withdrawal_amount)
            else:
                print("insuffcient balance")
        elif menu=="d":
            deposit_amount=int(input("enter the deposit amount"))
            if deposit_amount>0:
                print(current_balance+deposit_amount)
            else:
                print(current_balance)
    else:
        print("please enter valid pin")
else:
    current_balance=25000
    if language=="telugu":
        print("hdfc ki swagatham")
        print("mi card ni insert cheyandi")
        password=int(input("enter the pin"))
        pin=4040
        if pin==password:
            menu=input("mi option ni select cheskondi:")
            if menu=="b":
                if current_balance>0:
                    print(current_balance)
                else:
                    print("zero balance")
            elif menu=="w":
                withdrawal_amount=int(input("enter the amount"))
                if withdrawal_amount<=current_balance: 
                    print("trasation successful",current_balance-withdrawal_amount)
                else:
                    print("insuffcient balance")
            elif menu=="d":
                deposit_amount=int(input("enter the deposit amount"))
                if deposit_amount>0:
                   print(current_balance+deposit_amount)
                else:
                   print(current_balance)
    else:
        print("envaild language")