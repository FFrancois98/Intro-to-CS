my_list = [1, 7, 3, 5]
target_sum = 9

def HasPairWithTargetSum(my_list, target_sum):
    if len(my_list) < 2:
        return False
    
    my_dict = {}

    for i in my_list:
        halfp = target_sum - i
        my_dict[i] = halfp

    not_in_it = 0
    for key in my_dict:
        if key not in my_dict.values():
            not_in_it += 1
        if not_in_it == len(my_list):
            return False
            
        if key in my_dict.values():
            if key == my_dict[key]:
                key_count = my_list.count(key)
                if key_count < 2:
                    return False
                return True
            return True
        

print(HasPairWithTargetSum(my_list, target_sum))
