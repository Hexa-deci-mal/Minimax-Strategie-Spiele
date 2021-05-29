'''
Functions providing MinMaxAi with data
'''

# Returns a list of all possible moves
from typing import List


def getPossibleMoves():
    MoveList = []
    return MoveList


# Evaluates a score for a particular move
def scoreMove(player, move):
    Score = 0

    ScoreMultiWin = 10
    ScoreMultiNotLose = 7
    ScoreMultiProgress = 3
    ScoreMultiBlocked = 2
    
    ScoreWin = getScoreWin(move)
    ScoreNotLose = getScoreNotLose(move)
    ScoreProgress = getScoreProgress(move)
    ScoreBlocked = getScoreBlocked(move)

    ScoreWinFactored = ScoreWin * ScoreMultiWin
    ScoreNotLoseFactored = ScoreNotLose * ScoreMultiNotLose
    ScoreProgressFactored = ScoreProgress * ScoreMultiProgress
    ScoreBlockedFactored = ScoreBlocked * ScoreMultiBlocked

    Score = ScoreWinFactored + ScoreNotLoseFactored + ScoreProgressFactored + ScoreBlockedFactored

    return Score

#Evaluates if move can win
def getScoreWin(move):
    score = 0
    return score

    #Evaluates if move can avoid defeat
def getScoreNotLose(move):
    score = 0
    return score

    #Evaluates if move can create progress
def getScoreProgress(move):
    score = 0
    return score

    #Evaluates if move can block enemy
def getScoreBlocked(move):
    score = 0
    return score