a=15
b=12

for i in range(0,100000):
    x=(a//4+b**3)<2000 and (b%4!=0)
    print(x)
    x=(a//4+b**3)<2000 or (b%4!=0)
    print(x)