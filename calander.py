import calendar as cal


year = int(input("enter the year to see its calander :-->>"))

try:
    for i in range(1, 13):
        print(cal.month(year, i))
except ValueError:
    print("invalid")


