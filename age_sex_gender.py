# Accept the age, sex (‘M’, ‘F’), number of days and display the wages accordingly

# If age does not fall in any range then display the following message: “Enter appropriate age”
age=int(input("enter the age:"))
gender=input("enter the gender:")
days=int(input("enter the days:"))
if age>=18 and age<30:
    gender=="M"
    wages=700*days
    print("total amount",wages)
elif age>=18 and age<30:
    gender=="F"
    wages=750*days
    print("total amount",wages)
elif age>=30 and age<=40:
    gender=="M"
    wages=800*days
    print("total amount",wages)
elif age>=30 and age<=40:
    gender=="F"
    wages=800*days
    print("total amount",wages)
else:
    print("no salary")





