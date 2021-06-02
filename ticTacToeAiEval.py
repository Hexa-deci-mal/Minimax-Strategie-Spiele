'''
Functions providing MinMaxAi with score data for tictactoe
@author Lukas Eckert
'''


from arrayUtils import *
from typing import List
from moveEvaluation import *

from numpy import ndarray



# Returns a list of all possible moves
def getPossibleMovesInklScore(board:ndarray, player):
    ScoredMoveList = []
    MoveList = getEmptyPositions(board)

    #printYellowMsg("Inspect MoveList non empty pos")
    #print(MoveList)

    for move in MoveList:
        moveScore = scoreMove(player,move[0],move[1],board)
        ScoredMoveList.append([move,moveScore])

    return ScoredMoveList

# applies a move to a given board resulting in a new board
def applyVirtualMove(board:ndarray, player:int, move:List):
    virtualBoard = cloneBoard(board)

    setIfEmpty(move[0],move[1],player)
    
    return virtualBoard

# Evaluates a score for a particular move
def scoreMove(player:int, moveRowIndex:int, moveColumnIndex:int, board:ndarray):
    # score initialized as 0. Makes for a good middle ground dontcha think
    Score = 0

    #printErrorMsg(f"Inspecting move row:{moveRowIndex} column:{moveColumnIndex}")

    # Weight factor to be applied to each evaluation
    ScoreMultiWin = 10000
    ScoreMultiNotLose = 1000
    ScoreMultiProgress = 100
    ScoreMultiFree = 10
    ScoreMultiBlocked = 1


    enemyTile = player
    if(player == TILE_PLAYER_RED):
        enemyTile = TILE_PLAYER_WHITE
    else:
        enemyTile = TILE_PLAYER_RED



    # Gets simple move Scores
    ScoreWin = getScoreWin(moveRowIndex,moveColumnIndex,board,player)
    ScoreNotLose = getScoreNotLose(moveRowIndex,moveColumnIndex,board,enemyTile)
    ScoreProgress = getScoreProgress(moveRowIndex,moveColumnIndex,board,enemyTile)
    ScoreFree = getScoreFree(moveRowIndex,moveColumnIndex,board,player)
    ScoreBlocked = getScoreBlocked(moveRowIndex,moveColumnIndex,board,enemyTile)

    #print(f"ScoreWin:{ScoreWin}, ScoreNotLose:{ScoreNotLose}, ScoreProgress:{ScoreProgress}, ScoreBlocked:{ScoreBlocked}")

    # Factorizes Move Scores with weight values
    ScoreWinFactored = ScoreWin * ScoreMultiWin
    ScoreNotLoseFactored = ScoreNotLose * ScoreMultiNotLose
    ScoreProgressFactored = ScoreProgress * ScoreMultiProgress
    ScoreFreeFactored = ScoreFree * ScoreMultiFree
    ScoreBlockedFactored = ScoreBlocked * ScoreMultiBlocked

    #print(f"ScoreWinFactored:{ScoreWinFactored}, ScoreNotLoseFactored:{ScoreNotLoseFactored}, ScoreProgressFactored:{ScoreProgressFactored}, ScoreBlockedFactored:{ScoreBlockedFactored}, ScoreFreeFactored:{ScoreFreeFactored}")

    # Sums up individual scores to create master score
    Score = ScoreWinFactored + ScoreNotLoseFactored + ScoreProgressFactored + ScoreFreeFactored + ScoreBlockedFactored

    #print(f"Score Master:{Score}")

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
def getScoreNotLose(rowIndex:int, columnIndex:int, brd:ndarray, enemyTile:int):

    # Skip eval if move is forbidden
    if brd[rowIndex][columnIndex] != TILE_EMPTY:
        return -500

    numberOfLosses = getLossCounts(rowIndex,columnIndex,enemyTile,brd)

    return numberOfLosses

# Evaluates if move can create progress
def getScoreProgress(rowIndex:int, columnIndex:int, brd:ndarray, enemyTile:int):

    # Skip eval if move is forbidden
    if brd[rowIndex][columnIndex] != TILE_EMPTY:
        return -500

    numberOfProgressCounts = getProgressCounts(rowIndex,columnIndex,enemyTile,brd)

    return numberOfProgressCounts

# Evaluates if move can block enemy
def getScoreBlocked(rowIndex:int, columnIndex:int, brd:ndarray, enemyTile:int):
    score = getBlockedCounts(rowIndex,columnIndex,enemyTile,brd)
    return score

def getScoreFree(rowIndex:int, columnIndex:int, brd:ndarray, tile:int):
    score = getFreeCounts(rowIndex,columnIndex,tile,brd)
    return score