my_list = []
r_list = []  #sorted list
def ReverseList(my_list):
    size = len(my_list)
    index = size - 1
    for i in range(size):
        b = my_list[index]
        r_list.append(b)
        index -= 1
    return r_list

'''
def ReverseList(my_list):
    r_list = my_list[::-1]
    return r_list
'''

def IsPalindrome(my_list):
    if ReverseList(my_list) == my_list:
        return True
    return False

print(IsPalindrome(my_list))
