hour = int(input('Enter the hour '))
minute = int(input('Enter the minute '))

if 0 <= minute <= 59:
    if minute < 10:
        minute = '0' + str(minute)
    if minute == 0:
        minute = '00'
if 0 <= hour <= 11:
    if hour == 0:
        hour = 12
    print(hour, ':', minute, 'AM')
if 12 <= hour <= 23:
    if 13 <= hour <= 23:
        hour = hour - 12
    print(hour, ':', minute, 'PM')
