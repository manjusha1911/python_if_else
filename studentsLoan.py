# government provide student loan,for loan eligiblity age range must 17-21 ,and must have a minimum of 80% score
name=input("enter the name:")
age=int(input("enter the age:"))
score=int(input("enter the score:"))
if age>=17 and age<=21:
    if score>=80:
        print("eligible")
else:
    print("not eligible")