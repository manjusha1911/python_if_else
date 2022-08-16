time=int(input("enter the time"))
# time=(str(time))
if time>="6:15" and time<="7:00":
    print("exersise")
elif time>="8:00" and time<"8:30":
    print("breakfast")
elif time>="8:30" and time<"12:30":
    print("first coding")
elif time>="12:30" and time<"2:00":
    print("lunch")
elif time>="2:00" and time<"5:00":
    print("second coding")
elif time>="5:30" and time<"2:00":
    print("snacks break")
elif time>="6:00" and time<"7:00":
    print("english activity")
elif time>="7:00" and time<"8:00":
    print("recreation")
elif time>="8:00" and time<"9:00":
    print("dinner")
else:
    ("sleeping time")