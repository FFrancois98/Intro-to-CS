month = input('Enter month: ')
month = month.lower()
day = int(input('Enter day: '))

def GetDayOfYear(month, day):
    total_day = 0
    if month == 'january':
        total_day = day
    if month == 'february':
        total_day = day + 31
    if month == 'march':
        total_day = day + 59
    if month == 'april':
        total_day = day + 90
    if month == 'may':
        total_day = day + 120
    if month == 'june':
        total_day = day + 151
    if month == 'july':
        total_day = day + 181
    if month == 'august':
        total_day = day + 212
    if month == 'september':
        total_day = day + 243
    if month == 'october':
        total_day = day + 273
    if month == 'november':
        total_day= day + 304
    if month == 'december':
        total_day = day + 334
    return total_day

total_day = GetDayOfYear(month, day)
print(total_day)
