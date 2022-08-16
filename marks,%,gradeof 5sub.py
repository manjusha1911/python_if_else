# pysics,chemistry,english,mathematics and computer
# calculate percentage & grade
# percentage>=90%:grade:A
# percentage>=80%:grade:B
# percentage>=70%:grade:C
# percentage>=60%:grade:D
# percentage>=40%:grade:E
# percentage>=60%:grade:F
sub1=int(input("enter pysics marks:"))
sub2=int(input("enter chemistry marks:"))
sub3=int(input("enter english marks:"))
sub4=int(input("enter mathematics marks:"))
sub5=int(input("enter computer marks:"))
total_sub=sub1+sub2+sub3+sub4+sub5
percentage=(total_sub/500)*100
if percentage>=90:
    print("grade A")
elif percentage<90 and percentage>=80:
    print("grade B")
elif percentage<80 and percentage>=70:
    print("grade C")
elif percentage<70 and percentage>=60:
    print("grade D")
elif percentage<60 and percentage>=40:
    print("grade E")
else:
    print("grade F")