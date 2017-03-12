board_values = [[4, 4, 4],
                [4, 4, 4],
                [4, 4, 4]]
player = 'o'

rows = 3
cols = 3
pH = 0
for j in range(cols - 1, -1, -1):
    if j < rows - 1:
        pH += 1
    for i in range(rows - 1, -1, -1):
        r_d = i
        c_d = j

        count = 0
        while r_d >= pH:
            if board_values[r_d][c_d] == 4 and r_d < rows and c_d < cols:
                count += 1
            r_d -= 1
            c_d -= 1
        print(count)
        if count == 3:
            print('Hi!')



'''
if (None) in board_values[0]:
    print('h')
    
print(board_values)


def FillBoard():
    board_values[0][0] = player
    board_values[0][1] = player
    board_values[0][2] = player
    board_values[1][0] = player
    board_values[1][1] = player
    board_values[1][2] = player
    board_values[2][0] = player
    board_values[2][1] = player
    board_values[2][2] = player
    
FillBoard()

print(board_values)    


# matrix = [[None] * 8 for i in range(5)]
matrix = [[None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None]]

print(matrix)

for i in range(4, -1, -1): # ITs the rows minus 1
    if matrix[i][2] == None: # its the col index in the second bracket
        matrix[i][2] = 2
        break
print(matrix)

matrix[0][0]= 'blue'
matrix[1][0]= 'green'
matrix[2][0]= 'green'
matrix[3][0]= 'green'
matrix[4][0]= 'green'


def contains_sublist(lst, sublst):
    n = len(sublst)
    return any((sublst == lst[i:i+n]) for i in range(len(lst)-n+1))
print(contains_sublist(matrix, ['green'] *  4))


count = 0
for i in range(5):
    if matrix[i][0] == 'green':
        count += 1
    else:
        count = 0
    print(count)
if count >= 4:
    print('Win')


# this only works for horizintal correctness
# try counter variable for the columun that stays zero until right and if it
# back wrong then it restats at zero
# horizintal check should be in a for loop descending

print(matrix)
'''
