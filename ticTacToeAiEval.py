'''
Functions providing MinMaxAi with score data for checkers
@author Lukas Eckert
'''

# Returns a list of all possible moves
from arrayUtils import TILE_EMPTY
from typing import List
from moveEvaluation import *

from numpy import ndarray

'''
 Feeling useful, might delete later
'''
def getPossibleMovesInklScore(board:ndarray, player):
    ScoredMoveList = []
    MoveList = getEmptyPositions(board)

    printYellowMsg("Inspect MoveList non empty pos")
    print(MoveList)

    for move in MoveList:
        moveScore = scoreMove(player,move[0],move[1],board)
        ScoredMoveList.append([move,moveScore])

    return ScoredMoveList


# Evaluates a score for a particular move
def scoreMove(player:int, moveRowIndex:int, moveColumnIndex:int, board:ndarray):
    # score initialized as 0. Makes for a good middle ground dontcha think
    Score = 0

    printErrorMsg(f"Inspecting move row:{moveRowIndex} column:{moveColumnIndex}")

    # Weight factor to be applied to each evaluation
    ScoreMultiWin = 10
    ScoreMultiNotLose = 7
    ScoreMultiProgress = 3
    ScoreMultiBlocked = 2

    # Gets simple move Scores
    ScoreWin = getScoreWin(moveRowIndex,moveColumnIndex,board,player)
    ScoreNotLose = getScoreNotLose(moveRowIndex,moveColumnIndex,board,player)
    ScoreProgress = getScoreProgress(moveRowIndex,moveColumnIndex,board,player)
    ScoreBlocked = getScoreBlocked(moveRowIndex,moveColumnIndex,board,player)

    print(f"ScoreWin:{ScoreWin}, ScoreNotLose:{ScoreNotLose}, ScoreProgress:{ScoreProgress}, ScoreBlocked:{ScoreBlocked}")

    # Factorizes Move Scores with weight values
    ScoreWinFactored = ScoreWin * ScoreMultiWin
    ScoreNotLoseFactored = ScoreNotLose * ScoreMultiNotLose
    ScoreProgressFactored = ScoreProgress * ScoreMultiProgress
    ScoreBlockedFactored = ScoreBlocked * ScoreMultiBlocked

    print(f"ScoreWinFactored:{ScoreWinFactored}, ScoreNotLoseFactored:{ScoreNotLoseFactored}, ScoreProgressFactored:{ScoreProgressFactored}, ScoreBlockedFactored:{ScoreBlockedFactored}")

    # Sums up individual scores to create master score
    Score = ScoreWinFactored + ScoreNotLoseFactored + ScoreProgressFactored + ScoreBlockedFactored

    print(f"Score Master:{Score}")

    # return master score
    return Score

# Evaluates if move can win
def getScoreWin(rowIndex:int, columnIndex:int, brd:ndarray, playerTile:int):

    # Skip eval if move is forbidden
    if brd[rowIndex][columnIndex] != TILE_EMPTY:
        return -500

    numberOfWins = getWinCounts(rowIndex, columnIndex, playerTile, brd)

    return numberOfWins

# Evaluates if move can avoid defeat
def getScoreNotLose(rowIndex:int, columnIndex:int, brd:ndarray, playerTile:int):
    score = 0
    return score

# Evaluates if move can create progress
def getScoreProgress(rowIndex:int, columnIndex:int, brd:ndarray, playerTile:int):
    score = 0
    return score

# Evaluates if move can block enemy
def getScoreBlocked(rowIndex:int, columnIndex:int, brd:ndarray, playerTile:int):
    score = 0
    return score