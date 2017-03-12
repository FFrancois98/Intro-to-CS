total_minutes = float(input('Minutes: '))

num_hours = int(total_minutes // 60)

num_minutes = int((total_minutes % 60) // 1)

num_seconds = int((((total_minutes - (total_minutes // 1)) * 60) // 1))

print(num_hours, 'hours,', num_minutes, 'minutes,', num_seconds, 'seconds')
