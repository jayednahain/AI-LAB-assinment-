#a = int(input("enter frist number: "))
b = int(input("enter second number: "))


def fizz_buzz(b):
    if b%3==0:
        return print("Fizz")
    elif b%5==0:
        return print("Buzz")
    elif b%3==0 and b%5==0:
        return print("FizzBuzz")
    else:
        print(b)


fizz_buzz(b)