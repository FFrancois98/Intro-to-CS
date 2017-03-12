first_num = int(input('Enter 1st number: '))
sec_num = int(input('Enter 2nd number: '))
third_num = int(input('Enter 3rd number: '))

if first_num <= sec_num <= third_num or third_num <= sec_num <= first_num:
    middle_number = sec_num
elif sec_num <= first_num <= third_num or third_num <= first_num <= sec_num:
    middle_number = first_num
else:
    middle_number = third_num

print('The middle number is', middle_number, '.')
