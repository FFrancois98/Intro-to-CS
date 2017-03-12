my_list = [] #input list
n_list = []

def LowestNumber(my_list):
    bottom = my_list[0]
    for i in my_list:
        if i < bottom:
            bottom = i
    return bottom

def SortList(my_list):
    for i in range(len(my_list)):
        new_next_num = LowestNumber(my_list)
        n_list.append(new_next_num)
        my_list.remove(new_next_num)
    return n_list
        
x = SortList(my_list)

print(x)


