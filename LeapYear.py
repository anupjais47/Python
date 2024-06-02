num = int(input("Enter a year to check Leap or not : "))
if num<1:
    print(num," as a year not possible.")
elif num%100==0:
    if num%400==0:
        print(num," is a leap year.")
    else:
        print(num," not a leap year.")
elif num%4==0:
    print(num," is a leap year.")
else:
    print(num," is not a leap year.")
