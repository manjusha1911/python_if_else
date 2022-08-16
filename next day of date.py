#Write a Python program to get next day of a given date.
# Expected Output:
# Input a year: 2016                                                      
# Input a month [1-12]: 08                                                
# Input a day [1-31]: 23                                                  
# The next date is [yyyy-mm-dd] 2016-8-24
year=int(input("enter the year:"))
month=int(input("enter the month:"))
day=int(input("enter the day:"))
if month>=1 and month<=12:
    if day>=1 and day<31:
        print("day is","-",year,"-",month,"-",day+1)
    if day>=31:
        print("day is","-",year,"-",month,"-",day-30)
    else:
        print("wrong input")
else:
    print("enter valid day")


