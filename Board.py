import numpy as np
import Global_Vars
import Game


def create_board_checkers():
    #1 = KI, 2 = Mensch
    Global_Vars.board = np.zeros((6,6))
    Global_Vars.board[0][1] = 1
    Global_Vars.board[0][3] = 1
    Global_Vars.board[0][5] = 1
    Global_Vars.board[1][0] = 1
    Global_Vars.board[1][2] = 1
    Global_Vars.board[1][4] = 1

    Global_Vars.board[5][1] = 2
    Global_Vars.board[5][3] = 2
    Global_Vars.board[5][5] = 2
    Global_Vars.board[4][0] = 2
    Global_Vars.board[4][2] = 2
    Global_Vars.board[4][4] = 2
    return Global_Vars.board

def create_board_tictactoe():
    Global_Vars.board = np.zeros((6,6))
    return Global_Vars.board

def create_board_bauernschach():
    Global_Vars.board = np.zeros((6,6))
    Global_Vars.board[1][0] = 1
    Global_Vars.board[1][1] = 1
    Global_Vars.board[1][2] = 1
    Global_Vars.board[1][3] = 1
    Global_Vars.board[1][4] = 1
    Global_Vars.board[1][5] = 1

    Global_Vars.board[4][0] = 2
    Global_Vars.board[4][1] = 2
    Global_Vars.board[4][2] = 2
    Global_Vars.board[4][3] = 2
    Global_Vars.board[4][4] = 2
    Global_Vars.board[4][5] = 2
    return Global_Vars.board

Global_Vars.game_name = 'bauernschach'
Global_Vars.board = create_board_checkers()
Global_Vars.possible_moves = Game.get_Possible_Moves(Global_Vars.player, Global_Vars.board, Global_Vars.game_name)
#Global_Vars.pos_list_player = Game.current_Player_Pos_List(2)

print(Global_Vars.game_name)
print(Global_Vars.player)
#print(Global_Vars.pos_list_player)
print(Global_Vars.board)
print(Global_Vars.possible_moves)
#print(Global_Vars.board)



   

    
    


