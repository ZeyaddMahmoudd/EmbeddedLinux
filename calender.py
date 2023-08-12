import calendar
def print_calender(month, year):
    print(calendar.month_name[month], year)
    print("Mon  Tue  Wed  Thurs  Fri  Sat  Sun")

    cal = calendar.monthcalendar(2010,5)


    for week in cal:
        for day in week:

            if day == 0:
                print("     ", end = "")
            else:
                print(f"{day:2d}   ", end = "")
        print()

month = int(input("Please type the month : "))
year = int(input("Please type the year : "))

print_calender(month, year)