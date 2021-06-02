'''
Simple scoring algorithm only looking at the next possible move.
This evaluation is assembled from the first attempt at creating a valid scoring system.
'''

from ticTacToeAiEval import getPossibleMovesInklScore
from numpy import ndarray
import Global_Vars
import math
from moveEvaluation import *

def run_simple_algorithm(name, player, board:ndarray):

    if name == "bauernschach":
        pass
    
    elif name == "dame":

        movesAndScores = getPossibleMovesInklScore(board,player)

        highScore = -math.inf
        highScoreMove = []

        for entry in movesAndScores:
            if(entry[1] > highScore):
                highScore = entry[1]
                highScoreMove = entry[0]

        return [highScoreMove,highScore]

    elif name == "tictactoe":
        pass