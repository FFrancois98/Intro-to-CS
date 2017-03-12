def GetIntersectionSize(range_1_min, range_1_max, range_2_min, range_2_max):
    if (range_1_min == range_1_max) or (range_2_min == range_2_max):
        inter_size = 0
    elif range_2_min < range_1_max:
        inter_size = range_1_max - range_2_min
    elif range_1_max < range_2_min:
        inter_size = -1
    return inter_size


# You don't need to change anything below this line.
range_1_min = int(input('Enter the min number for range 1: '))
range_1_max = int(input('Enter the max number for range 1: '))
range_2_min = int(input('Enter the min number for range 2: '))
range_2_max = int(input('Enter the max number for range 2: '))


intersection_size = GetIntersectionSize(
    range_1_min, range_1_max, range_2_min, range_2_max)
print('The intersection size is', intersection_size)


