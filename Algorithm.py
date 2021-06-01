from numpy import ndarray
from arrayUtils import setIfEmpty
from Board import create_board_tictactoe
import Global_Vars
import math
import ticTacToeAiEval
import moveEvaluation
import Game

#Running a Minimax Algorithm depending on which game is currently active
board = create_board_tictactoe()
def run_Algorithm(game_name, player, board:ndarray, depth:int):

    if Global_Vars.game_name == 'bauernschach':
        pass
    
    elif Global_Vars.game_name == 'dame':
        pass   

    elif Global_Vars.game_name == 'tictactoe':
        boardcopy = []        
        empty_positions = moveEvaluation.getEmptyPositions(board)
        if depth > 0:
            for move in empty_positions:
                tempcopy = board.copy()
                setIfEmpty(move[0], move[1], tempcopy, player)
                boardcopy.append(tempcopy)
                
                if Global_Vars.player == 1:
                    Global_Vars.player = 2
                elif Global_Vars.player == 2:
                    Global_Vars.player = 1
        print (boardcopy)

run_Algorithm('tictactoe', Global_Vars.player, board)
          
'''
    elif Global_Vars.game_name == 'tictactoe':
        Move_List = ticTacToeAiEval.getPossibleMovesInklScore(Global_Vars.board, Global_Vars.player)
        winning_moves = []
        losing_moves = []
        draw_moves = []
        valued_moves = []
        score = 0
        winning_move= +math.inf
        losing_move = -math.inf
        draw_move = 0   
        ending_move = False    
        for move in Move_List:           
            if move[1] == winning_move:
                ending_move = True
                score = +math.inf
                winning_moves.append(move)
                return ending_move, score
            
            if move[1] == losing_move:
                ending_move = True
                score = -math.inf
                losing_moves.append(move)
                return ending_move, score

            if move[1] == draw_move:
                draw_moves.append(move)
            
            if  move[1] == 1 or move[1] == 2 or move[1] == 3:
                valued_moves.append(move)
                score = score + move[1]
                return score
'''
           
