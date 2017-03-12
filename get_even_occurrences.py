my_list = []
def GetEvenNumOccurrences(my_list):
    my_dict = {}
    for char in my_list:
        if char in my_dict:
            my_dict[char] += 1
        else:
            my_dict[char] = 1
    
    even_list = []
    for i in my_dict:
        if my_dict[i] % 2 == 0:
            even_list.append(i)
    return even_list

print(GetEvenNumOccurrences(my_list))
