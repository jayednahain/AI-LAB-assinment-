a = int(input("enter a number for limitation: "))

for i in range(0,a+1):
    if i%2 != 0:
        print(i," ODD")
    elif i%2== 0:
        print(i, " EVEN")