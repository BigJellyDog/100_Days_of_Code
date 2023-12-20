year = int(input("Write a year: "))

if year % 4 == 0:
    if year % 100 == year % 400:
        print("Leap year")
    elif year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Not leap year")
else:
    print("Not leap year")
