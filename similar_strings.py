string_1 = 'turkey'
string_2 = 'tuney'

def AreSimilarStrings(string_1, string_2):

    diff_len = abs(len(string_1) - len(string_2))

    if diff_len > 1:
        return False

    if diff_len <= 1:
        c1 = 0 #shortest string index count
        c2 = 0 #longest string index count
        diff_char = 0 
        if len(string_1) > len(string_2):
            for i in range(len(string_2)):
                if string_2[c1] == string_1[c2]:
                    c1 += 1
                    c2 += 1
                elif string_2[c1] != string_1[c2]:
                    c2 += 1
            if c1 != c2:
                if string_2[c1] != string_1[c2]:
                    diff_char += 1
            if c2 - c1 > 1:
                return False
            elif diff_char >= 1:
                return False
            else:
                return True 
        elif len(string_2) > len(string_1):
            for i in range(len(string_1)):
                if string_1[c1] == string_2[c2]:
                    c1 += 1
                    c2 += 1
                elif string_1[c1] != string_2[c2]:
                    c2 += 1
            if c1 != c2:
                if string_1[c1] != string_2[c2]:
                    diff_char += 1             
            if c2 - c1 > 1:
                return False
            elif diff_char >= 1:
                return False
            else:
                return True
        elif len(string_2) == len(string_1):
            for i in range(len(string_1)):
                if string_1[i] != string_2[i]:
                    diff_char += 1
            if diff_char > 1:
                return False
            else:
                return True

print(AreSimilarStrings(string_1, string_2))
