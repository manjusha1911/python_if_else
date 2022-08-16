# calculate basic salary of employee its gross salary 
# HRA=house rent allowance
# DA=dearness allowance
# basic salary<=10000:HRA=20%,DA=80%
# basic salary<=20000:HRA=25%,DA=90%
# basic salary>20000:HRA=30%,DA=95%

# basic_salary=int(input("enter the salary:"))
# if basic_salary<=10000:
#     HRA=basic_salary*20/100
#     DA=basic_salary*80/100
#     print(basic_salary+HRA+DA)
# elif basic_salary>10000 and basic_salary<=20000:
#     HRA=basic_salary*25/100
#     DA=basic_salary*90/100
#     print(basic_salary+HRA+DA)
# else:
#     HRA=basic_salary*30/100
#     DA=basic_salary*95/100
#     print(basic_salary+HRA+DA)
basic_salary=float(input("enter the salary:"))
if basic_salary<=10000:
    HRA=basic_salary*0.2
    DA=basic_salary*0.8
    print(basic_salary+HRA+DA)
elif basic_salary>10000 and basic_salary<=20000:
    HRA=basic_salary*0.25
    DA=basic_salary*0.9
    print(basic_salary+HRA+DA)
else:
    HRA=basic_salary*0.3
    DA=basic_salary*0.95
    gross_salary=basic_salary+HRA+DA
    pf=0.12*basic_salary
    net_salary=gross_salary-pf
    print("name:",name)
    print("basic salary:",basic_salary)
    print("gross_salary:",gross_salary)
    print("net_salary:",net_salary)
