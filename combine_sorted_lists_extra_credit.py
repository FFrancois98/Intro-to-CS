list_1 = [[ ], [1, 3], [ ], [2]]
def CombineSortedLists(list_1):    
    list_2 = []
    list_3 = []
    
    for i in list_1:
        list_2 += i
    
    for i in range(len(list_2[:])):
        mini = min(list_2)
        list_3.append(mini)
        list_2.remove(mini)
    print(list_3)

CombineSortedLists(list_1)
