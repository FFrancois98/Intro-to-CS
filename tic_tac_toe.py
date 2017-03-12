from tic_tac_toe_graphics import *


def BoardClicked(col_index, row_index):
        global player
        
        if board_values[row_index][col_index] == None:
                print('BoardClicked col_index:', col_index, 'row_index:',
                      row_index)
                board.mark_square(col_index, row_index, player)
                board_values[row_index][col_index] = player
                
                if player == board_values[0][0] and \
                   player == board_values[0][1] and \
                   player == board_values[0][2]:
                        board.display_message('Player ' + player + ' won!')
                        FillBoard()

                elif player == board_values[1][0] and \
                     player == board_values[1][1] and \
                     player == board_values[1][2]:
                        board.display_message('Player ' + player + ' won!')
                        FillBoard()
                        
                elif player == board_values[2][0] and \
                     player == board_values[2][1] and \
                     player == board_values[2][2]:
                        board.display_message('Player ' + player + ' won!')
                        FillBoard()

                elif player == board_values[0][0] and \
                     player == board_values[1][0] and \
                     player == board_values[2][0]:
                        board.display_message('Player ' + player + ' won!')
                        FillBoard()

                elif player == board_values[0][1] and \
                     player == board_values[1][1] and \
                     player == board_values[2][1]:
                        board.display_message('Player ' + player + ' won!')
                        FillBoard()

                elif player == board_values[0][2] and \
                     player == board_values[1][2] and \
                     player == board_values[2][2]:
                        board.display_message('Player ' + player + ' won!')
                        FillBoard()

                elif player == board_values[0][0] and \
                     player == board_values[1][1] and \
                     player == board_values[2][2]:
                        board.display_message('Player ' + player + ' won!')
                        FillBoard()

                elif player == board_values[0][2] and \
                     player == board_values[1][1] and \
                     player == board_values[2][0]:
                        board.display_message('Player ' + player + ' won!')
                        FillBoard()
                        
                elif (None) not in board_values[0] and \
                     (None) not in board_values[1] and \
                     (None) not in board_values[2]:
                        board.display_message('It\'s a draw :(')                       

                else:
                        if player == 'x':
                                player = 'o'
                        else:
                                player = 'x'
                        print(player)
                        board.display_message('It\'s Player ' + player +
                                              '\'s turn!')
                               
                return player
                

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
    
player = 'x'
board = TicTacToeBoard(3, 3, BoardClicked)
board_values = [[None, None, None],
                [None, None, None],
                [None, None, None]]

board.display_message('It\'s Player ' + player + '\'s turn!')

# Make sure mainloop() is the last line of code in this program!
mainloop()

