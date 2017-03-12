year = int(input('Enter year: '))

def IsLeapYear(year):
    leap_year = False
    if (year % 4 == 0) and (year % 100 == 0) and (year % 400 == 0):
        leap_year = 'True'
    elif (year % 4 == 0) and (year % 100 == 0):
        leap_year = 'False'
    elif (year % 4 == 0):
        leap_year = 'True'            
    return leap_year

print(IsLeapYear(year))
