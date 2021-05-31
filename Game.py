import Global_Vars
import numpy
import os



def current_Player_Pos_List(player):    
    board = Global_Vars.board
    pos_list_player = []
    for row in range(len(board)):
        for cell in range(len(board[row])):
            if board[row][cell] == player:
                pos_list_player.append([row, cell])
    return pos_list_player

#Getting all possible moves for the current state of the board, from the human perspective.
def get_Possible_Moves(player, board, game_name):
    
    possible_moves = []
    for row in range(len(board)):
        for cell in range(len(board[row])):  
            if player == 2:
                if game_name == 'dame':
                    pass  

                elif game_name == 'bauernschach':
                    if board[row][cell] == player:
                        #Move Up possible?
                        if board[row-1][cell] != 2 and board[row-1][cell] == 0:
                            #[row, cell, beat enemy piece?, Winning Move?]
                            if row-1 == 0:
                                possible_moves.append([row, cell, row-1, cell, False, True])
                            else:
                                possible_moves.append([row, cell, row-1, cell, False, False])
                        
                        #Move to up-left possible?
                        if cell - 1 >= 0:  
                            if board[row-1][cell-1] != 2 and board[row-1][cell-1] != 0 and row-1 == 0:
                                possible_moves.append([row, cell, row-1, cell -1, True, True])                  
                            elif board[row-1][cell-1] != 2 and board[row-1][cell-1] != 0 and row-1 != 0:
                                possible_moves.append([row, cell, row-1, cell -1, True, False])
                                
                        #Move to up right possible?                  
                        if cell + 1 <= 5:
                            if board[row-1][cell-1] != 2 and board[row-1][cell+1] != 0 and row-1 == 0:
                                possible_moves.append([row, cell, row-1, cell+1, True, True])                  
                            elif board[row-1][cell-1] != 2 and board[row-1][cell+1] != 0 and row-1 != 0:
                                possible_moves.append([row, cell, row-1, cell+1, True, False])
                    Global_Vars.player = 1       

                elif game_name == 'tictactoe':
                    if board[row][cell] != player == 0:
                        possible_moves.append([row, cell, False, False])
                    Global_Vars.player = 1
                
                        
            elif player == 1:         
                if game_name == 'dame':
                    pass  

                elif game_name == 'bauernschach':
                    if board[row][cell] == player:
                        #Moving possible?
                        if board[row+1][cell] != 1 and board[row+1][cell] == 0:
                            #[cur_row, cur_cell, new_row, new_cell, beat enemy piece?, Winning Move?]
                            if row+1 == 5:
                                possible_moves.append([row, cell, row+1, cell, False, True])
                            else:
                                possible_moves.append([row, cell, row+1, cell, False, False])
                                    
                        #Moving up-left possible?
                        if cell +1 <= 5:  
                            if board[row+1][cell-1] != 0 and board[row+1][cell-1] != 1 and row+1 == 5:
                                possible_moves.append([row, cell, row+1, cell -1, True, True])                  
                            elif board[row+1][cell-1] != 0 and board[row+1][cell-1] != 1 and row+1 != 5:
                                possible_moves.append([row, cell, row+1, cell -1, True, False])
                                            
                        #Moving up right possible?                  
                        if cell + 1 <= 5:
                            if board[row+1][cell+1] != 0 and board[row+1][cell-1] != 1 and row+1 == 5:
                                possible_moves.append([row, cell, row+1, cell+1, True, True])                  
                            elif board[row+1][cell+1] != 0 and board[row+1][cell-1] != 1 and board[row+1][cell+1] != 1 and row+1 != 5:
                                possible_moves.append([row, cell, row+1, cell+1, True, False])                              
                        elif game_name == 'tictactoe':
                            pass
                    Global_Vars.player = 2

                elif game_name == 'tictactoe':
                    pass
               
    return possible_moves


def calc_Score():
    pass


