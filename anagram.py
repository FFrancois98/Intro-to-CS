string = 'hot dog'
string_2nd = 'potato'
def IsAnagram(string, string_2nd):
    empty_dict = {}
    empty_2 = {}

    for char in string:
        val = string.count(char)
        if char not in empty_dict:
            empty_dict[char] = val

    for char in string_2nd:
        vals = string_2nd.count(char)
        if char not in empty_2:
            empty_2[char] = vals

    if ' ' in empty_dict:
        del empty_dict[' ']

    if ' ' in empty_2:
        del empty_2[' ']

    if empty_2 == empty_dict:
        return True
    else:
        return False

print(IsAnagram(string, string_2nd))
