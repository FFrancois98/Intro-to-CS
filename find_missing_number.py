list_1 = [-6, -11, -8, -9, -10]

def FindMissingNumber(list_1):
    miss = 0

    for i in list_1:
        miss = i + 1
        if miss not in list_1 and (min(list_1) < miss < max(list_1)):
           print(miss)

FindMissingNumber(list_1)
