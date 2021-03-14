a = int(input("enter a speed: "))

def check_speed(speed):
    count = 0
    if speed<70:
        print("OK")

    elif speed>70:
        for i in range(70,speed,5):
            count = count+1
            print("points: ",count)
            if count>12:
                return print("License suspended")
        return print(speed)
        


check_speed(a)