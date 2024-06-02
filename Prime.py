num=int(input("Enter a number to check prime or not : "))
if num>1:
    numm=num//2
    for i in range(2,numm+1) :
        if num%i==0 :
            print(f"{num} is not a prime.")
            break
    else :
        print(f"{num} is a prime.")
else:
    print("For the checking prime {num}, is not a valid number.🙏")
    