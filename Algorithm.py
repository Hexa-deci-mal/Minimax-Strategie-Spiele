from printUtils import printErrorMsg
from ticTacToe import checkIfWin
from numpy import ndarray
from arrayUtils import setIfEmpty
from Board import create_board_tictactoe
import Global_Vars
import math
import ticTacToeAiEval
import moveEvaluation
import Game

#Running a Minimax Algorithm depending on which game is currently active
#board = create_board_tictactoe()
def run_Algorithm(game_name, player, board:ndarray, depth:int):

    printErrorMsg(f"AHHHHHHHHHHHHHHHHHHHHHHH {depth}")

    if Global_Vars.game_name == 'bauernschach':
        pass
    
    elif Global_Vars.game_name == 'dame':
        pass   

    elif Global_Vars.game_name == 'tictactoe':
        boardcopy = []       
        #checkIfWin(board, player, False)
        empty_positions = moveEvaluation.getEmptyPositions(board)

        nextPlayer = player + 1
        if(nextPlayer == 3):
            nextPlayer = 1

        maxxedMinnedScores = []

        for move in empty_positions:
            tempcopy = board.copy()
            setIfEmpty(move[0], move[1], tempcopy, player)
            boardcopy.append(tempcopy)
            
            if depth > 0:
                maxxedMinnedScores.append(run_Algorithm(game_name,nextPlayer,tempcopy,depth -1))
            else:
                # eval for base case results
                moves = ticTacToeAiEval.getPossibleMovesInklScore(tempcopy,nextPlayer)
                print(nextPlayer)

                highestScore = -math.inf
                highestMove = []

                lowestScore = math.inf
                lowestMove = []

                for entry in moves:
                    if entry[1] > highestScore:
                        #print (f"Entry:{entry[1]}, high:{highestScore}, comp:{entry[1] > highestScore}")
                        highestScore = entry[1]
                        highestMove = entry[0]
                    if entry[1] < lowestScore:
                        #print (f"Entry:{entry[1]}, low:{lowestScore}, comp:{entry[1] > lowestScore}")
                        lowestScore = entry[1]
                        lowestMove = entry[0]
                    
                if depth == 0:
                    return [highestMove,highestScore]
                
                if depth % 2:
                    return [highestMove,highestScore]
                return [lowestMove,lowestScore]
        # eval for recursive results

        highestScoreMain = -math.inf
        highestMoveMain = []

        lowestScoreMain = math.inf
        lowestMoveMain = []

        for entry in maxxedMinnedScores:
            if entry[1] > highestScoreMain:
                highestScoreMain = entry[1]
                highestMoveMain = entry[0]
            if entry[1] < lowestScoreMain:
                lowestScoreMain = entry[1]
                lowestMoveMain = entry[0]

        if depth == 0:
            return [highestMoveMain,highestScoreMain]

        if depth % 2:
            return [highestMoveMain,highestScoreMain]
        return [lowestMoveMain,lowestScoreMain]


#run_Algorithm('tictactoe', Global_Vars.player, board)
          
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
           
