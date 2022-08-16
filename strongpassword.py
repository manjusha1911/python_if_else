password=input("enter the password:")
length=len(password)
if length>=6 and length<=9:
    if 'A' in password or 'B' in password or 'C' in password or 'D' in password or 'E' in password or 'F' in password or 'I' in password or 'J' in password or 'K' in password or 'L' in password or 'M'in password or 'N' in password or 'O' in password or 'P' in password or 'Q' in password or'R'in password or 'S' in password or 'T' in password or 'U' in password or 'V' in password or 'W'in password or 'X' in password or 'Y' in password or 'Z' in password:
        if 'a' in password or 'b' in password or 'c' in password or 'd' in password or 'e' in password or 'f' in password or 'i' in password or 'j' in password or 'k' in password or 'l' in password or 'm' in password or 'n' in password or 'o' in password or 'P' in password or 'q' in password or 'r'in password or 's' in password or 't' in password or 'u' in password or 'v' in password or 'w' in password or 'x' in password or 'y' in password or 'z' in password:
            if "@" or '&' or "#" or "$" or "&" or "!" or "*" in password:
                if "1" or '2' or "3" or "4" in password:
                    print("strong password")
                else:
                    print("atleast one digit must contain in your password")
            else:
                print("special charactor is missed")
        else:
            print("samll letters are missed")
    else:
        print("capital letter is missed")
else:
    print("password must contain more thna 6 characters")
