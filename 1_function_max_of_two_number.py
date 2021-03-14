a = int(input("enter number one: "))
b = int(input("enternumber two:"))
def max(z,y):
    if a>b:
        return print("max value:",a," a is bigger then b")
    elif a<b:
        return print("max value is:",b," b is bigger then a")
    else:
        return print("both value is equal")


max(a,b)  