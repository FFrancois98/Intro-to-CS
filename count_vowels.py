def CountVowels(string):
    count_v = 0
    for x in range(len(string)):
        if string[x] == 'a' or string[x] == 'e' or string[x] \
           == 'i' or string[x] == 'o' or string[x] == 'u':
            count_v += 1
    return count_v
print(CountVowels(''))
