

from ticTacToe import checkIfWin
from typing import List
from moveEvaluation import getEmptyPositions, getWinCounts
from numpy import ndarray


def doTicTacToeMinMax(depth:int, board:ndarray, currentplayer:int, evalPlayer:int, takenMove:List):

    moves:List = getEmptyPositions(board)

    if len(moves) == 1:
        return [moves[0],scoreEndState(currentplayer,evalPlayer,0)]

    if depth == 1 or len(moves) == 1:
        return [moveChosen,scoreCalculated]

    if checkIfWin(board,currentplayer):
        return [takenMove,scoreEndState(currentplayer,evalPlayer,100000)]


    return doTicTacToeMinMax(depth - 1, )

# adjust score
def scoreEndState(currentPlayer:int, evalPlayer:int, scoreRaw:int):
    mod = 1
    if currentPlayer != evalPlayer:
        mod = -1

    return scoreRaw * mod

# get move with highest score
def getHighestScoreMove(scoredMoves:List):
    highScore = 0
    moveEntry = []
    # Loop through entries
    for entry in scoredMoves:
        currentMove = entry[0]
        currentScore = entry[1]
        # Update highest
        if currentScore > highScore:
            highScore = currentScore
            moveEntry = currentMove