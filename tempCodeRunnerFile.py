# from tt
def cheak(vehicle):
    if len(vehicle)==10:
        if vehicle[0:2].isalpha() and vehicle[:2].isupper():
            if vehicle[2:4].isdigit():
                if vehicle[4:6].isalpha() and vehicle[6:8].isupper():
                    if vehicle[6:9].isdigit():
                        print("the number plate is valid")
                        return
    print("the number plate id not valid")

vehicle = input("Enter your vehicle number>>>>>>>>")
print("-----------------------------")
cheaking = cheak(vehicle)
