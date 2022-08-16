# first 5 days:Rs.2/day
# six to ten days:Rs.3/day
# ten to 15 days:Rs.4/day
# after 15 days:Rs.5/day
days=int(input("enter the days:"))
if days<=5:
    print(days*2)
elif days>=6 and days<=10:
    print(days*3)
elif days>10 and days<=15:
    print(days*4)
elif days>15:
    print(days*5)
else:
    print("enter valid input")