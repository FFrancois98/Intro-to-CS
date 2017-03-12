from connect_four_graphics import *

def BoardClicked(col_index):
    global player    
    win_sublst = [player] * chips_win
    
    print('BoardClicked col_index:', col_index)    
    for i in range(rows - 1, -1, -1):#its the rows minus 1
        if board_val[i][col_index] == None:
            #its the col index in the second bracket
            board_val[i][col_index] = player
            board.add_chip(col_index, i, player)
            break
    
    if CheckVertiWinner():
        board.display_message('Player ' + player + ' won!!!!')
        FillBoard()
        
    elif CheckHoriTotalWinner(win_sublst):
        board.display_message('Player ' + player + ' won!!!!')
        FillBoard()
        
    elif CheckRightDiagonal():
        board.display_message('Player ' + player + ' won!!!!')
        FillBoard()
        
    elif CheckLeftDiagonal():
        board.display_message('Player ' + player + ' won!!!!')
        FillBoard()

    elif IfBoardDraw():
        board.display_message('It\'s a draw. oh poo')
        
    else:                
        if player == 'green':
                player = 'red'
                board.display_message('It\'s Player ' + player + '\'s turn.')
        else:
                player = 'green'
                board.display_message('It\'s Player ' + player + '\'s turn.')
    
rows = int(input('Enter num of rows: '))
cols = int(input('Enter num of cols: '))
chips_win = int(input('Enter num of chips to win: '))

board = ConnectFourBoard(rows, cols, BoardClicked)

board_val = [[None] * cols for i in range(rows)]
player = 'green'
board.display_message('It\'s Player ' + player + '\'s turn.')

def CheckHoriWinner(lst, sublst):
    n = len(sublst)
    return any((sublst == lst[i : i + n]) for i in range(len(lst)- n + 1))

def CheckHoriTotalWinner(win_sublst):
    for i in range(rows):
        if CheckHoriWinner(board_val[i], win_sublst):
            return True
    return False

def CheckVertiWinner():
    count = 0
    for i in range(cols):
        for j in range(rows):
            if board_val[j][i] == player:
                count += 1
            else:
                count = 0
        if count >= chips_win:
            return True            
    return False
    
def CheckRightDiagonal():
    last_r = 0 # last row diagonal to check
    for j in range(cols):
        if cols - j < rows:
            last_r += 1
        for i in range(rows - 1, -1, -1):
            r_d = i # the row diagonal index
            c_d = j # the column diagonal index

            count = 0
            while r_d >= last_r:
                if board_val[r_d][c_d] == player and r_d < rows and c_d < cols:
                    count += 1
                else:
                    count = 0
                r_d -= 1
                c_d += 1
                if count >= chips_win:
                    return True
    return False

def CheckLeftDiagonal():
    last_r = 0
    for j in range(cols - 1, -1, -1):
        if j < rows - 1:
            last_r += 1
        for i in range(rows - 1, -1, -1):
            r_d = i # the row diagonal index
            c_d = j # the column diagonal index

            count = 0
            while r_d >= last_r:
                if board_val[r_d][c_d] == player and r_d < rows and c_d < cols:
                    count += 1
                else:
                    count = 0
                r_d -= 1
                c_d -= 1
                if count >= chips_win:
                    return True
    return False

def IfBoardDraw():
    count = 0
    for i in range(rows):
        if (None) not in board_val[i]:
            count += 1
    if count == rows:
        return True
    return False

def FillBoard():
    for i in range(rows):
        for j in range(cols):
            board_val[i][j] = player    
               
# Make sure mainloop() is the last line of code in this program!
mainloop()
