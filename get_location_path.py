from locations import location_dict

city = input('Enter a location: ').lower()

if city not in location_dict:
    if city in location_dict.values():
        print(city)
    else:
        print('Location not accessible')

else:
    while city in location_dict:
        val = location_dict[city]    
        print(city, end=', ')
        city = val
    print(val, end=' ')

