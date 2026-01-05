leap_year = False

year = int(input("Enter the year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    leap_year = True

months = {
    1: ("January", 31),
    2: ("February", 28),
    3: ("March", 31),
    4: ("April", 30),
    5: ("May", 31),
    6: ("June", 30),
    7: ("July", 31),
    8: ("August", 31),
    9: ("September", 30),
    10: ("October", 31),
    11: ("November", 30),
    12: ("December", 31)
}
if leap_year:
    months[2] = ("February", 29)
input_month = int(input("Enter the month number (1-12): "))
if input_month in months:
    month_name, days = months[input_month]
    print(f"Month {input_month} has {days} days and is {month_name} and the year {year} is", end=' ')
    if leap_year:
        print("a leap year.")
    else:
        print("not a leap year.")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")
