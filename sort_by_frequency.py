my_list = [5, 4, 5, 6, 5, 7, 8]
def SortByFrequency(my_list):
    list_2 = [] #elements of the original list
    list_3 = [] #count of elements in the original list
    list_4 = []

    for i in my_list:
        n1 = my_list.count(i)
        if i not in list_2:
            list_2.append(i)
            list_3.append(n1)

    for i in list_3[:]:
        n2 = max(list_3)
        n3 = list_3.index(max(list_3))
        for i in range(n2):
            list_4.append(list_2[n3])
        list_2.pop(n3)
        list_3.pop(n3)

    print(list_4)

SortByFrequency(my_list)
