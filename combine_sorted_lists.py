list_1 = []
list_2 = [1, 2]

def CombineTwoSortedLists(list_1, list_2):
    list_3 = list_1 + list_2
    list_4 = []
    
    for i in range(len(list_3[:])):
        mini = min(list_3)
        list_4.append(mini)
        list_3.remove(mini)
    print(list_4)
    
CombineTwoSortedLists(list_1, list_2)
