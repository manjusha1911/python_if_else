amount=int(input("enter the number:"))
if amount>=2000:
    n_2000=amount//2000
    amount=amount-n_2000*2000
    print(2000,"=",n_2000)
if amount>=500:
    n_500=amount//500
    amount=amount-n_500*500
    print(500,"=",n_500)
if amount>=200:
    n_200=amount//200
    amount=amount-n_200*200
    print(200,"=",n_200)
if amount>=100:
    n_100=amount//100
    amount=amount-n_100*100
    print(100,"=",n_100)
if amount>=50:
    n_50=amount//50
    amount=amount-n_50*50
    print(50,"=",n_50)
if amount>=20:
    n_20=amount//20
    amount=amount-n_20*20
    print(20,"=",n_20)
if amount>=10:
    n_10=amount//10
    amount=amount-n_10*10
    print(10,"=",n_10)
else:
    print("enter valid note")


