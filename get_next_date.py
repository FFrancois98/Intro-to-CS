month = int(input('Enter month: '))
day = int(input('Enter day: '))
year = int(input('Enter year: '))

def GetNextDate(month, day, year):
    day += 1
    if month == 1 and day > 31:
        day = 1
        month += 1
    if month == 2 and day > 28:
        day = 1
        month += 1
    if month == 3 and day > 31:
        day = 1
        month += 1
    if month == 4 and day > 30:
        day = 1
        month += 1
    if month == 5 and day > 31:
        day = 1
        month += 1
    if month == 6 and day > 30:
        day = 1
        month += 1
    if month == 7 and day > 31:
        day = 1
        month += 1
    if month == 8 and day > 31:
        day = 1
        month += 1
    if month == 9 and day > 30:
        day = 1
        month += 1
    if month == 10 and day > 31:
        day = 1
        month += 1
    if month == 11 and day > 30:
        day = 1
        month += 1
    if month == 12 and day > 31:
        day = 1
        month = 1
        year += 1
    month = str(month)
    day = str(day)
    year = str(year)
    next_date = month + '/' + day + '/' + year
    return next_date

next_date = GetNextDate(month, day, year)
print(next_date)
