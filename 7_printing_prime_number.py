limit = int(input("enter the limit: "))

def prime_number(limit):
    lower_limit = 0
    for num in range(lower_limit,limit+1):
        if num>1:
            for i in range(2,num):
                if(num%i) ==0:
                    break
            else:
                print(num)