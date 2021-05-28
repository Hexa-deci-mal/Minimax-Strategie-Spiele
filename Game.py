import Global_Vars
import numpy



def current_Player_Pos_List(player):    
    board = Global_Vars.board
    pos_list_player = []
    for row in range(len(board)):
        for cell in range(len(board[row])):
            if board[row][cell] == player:
                pos_list_player.append([row, cell])
    Global_Vars.pos_list_player = pos_list_player

def get_Possible_Moves_Human():
    player = Global_Vars.player
    board = Global_Vars.board
    game_name = Global_Vars.game_name
    winning_move = False
    possible_moves = []
    for row in range(len(board)):
        for cell in range(len(row)):            
            if game_name == 'dame':
                pass  

            if game_name == 'bauernschach':

                if board[row-1][cell] != player == 0:
                    #[row, cell, beat enemy piece?, Winning Move?]
                    if player == 2 and row-1 == 0:
                        possible_moves.append([row-1, cell, False, True])
                    else:
                          possible_moves.append([row-1, cell, False, False])
                
                #Move to up-left possible?
                if cell - 1 >= 0:
                    if board[row-1][cell-1] != player != 0:
                        possible_moves.append([row-1, cell-1, True]) 
                #Move to up right possible?                  
                if cell + 1 <= 6:
                    if board[row-1][cell+1] != player != 0:
                        possible_moves.append([row-1, cell+1, True])
            if game_name == 'tictactoe':
                if board[row][cell] != player == 0:
                    possible_moves.append([row, cell, True])

def traverse_Diagnonal(player):
    if player == 1:
        pass

    elif player == 2:
        pass

def traverse_Straight(player):
    pass

def bauernschach_Possible_Moves_KI():
    pass

def dame_Possible_KI():
    pass

def calc_Score():
    pass
