'''
Functions for movement evaluation (currently only for checkers)
@author Lukas Eckert
'''

from printUtils import printErrorMsg, printYellowMsg
import numpy
from arrayUtils import getNonEmptyPositions
from typing import List
from numpy import *

# Gets valid positions around piece
def getValidPositionsAroundPiece(rowPiece,columnPiece,board:ndarray):
    return getPositionsWithinBounds(getPositionsAroundPiece(rowPiece,columnPiece),board.shape[0] - 1,board.shape[1] - 1)

# Returns all positions surrounding a piece
def getPositionsAroundPiece(rowPiece, columnPiece):
    PosAround = []
    PosAround.extend(getHorizontalPos(rowPiece,columnPiece))
    PosAround.extend(getVerticalPos(rowPiece,columnPiece))
    PosAround.extend(getDiagonalPos(rowPiece,columnPiece))
    return PosAround

# returns possible horizontal coords
def getHorizontalPos(rowPos,columnPos):
    columnMin = columnPos - 1
    columnMax = columnPos + 1
    return [[rowPos,columnMin],[rowPos,columnMax]]

# returns possible Vertical coords
def getVerticalPos(rowPos,columnPos):
    rowMin = rowPos - 1
    rowMax = rowPos + 1
    return [[rowMin,columnPos],[rowMax,columnPos]]

# Returns possible Diagonal coords
def getDiagonalPos(rowPos,columnPos):
    rowMin = rowPos - 1
    rowMax = rowPos + 1
    columnMin = columnPos - 1
    columnMax = columnPos + 1
    return [[rowMin,columnMin],[rowMax,columnMin],[rowMin,columnMax],[rowMax,columnMax]]

# Returns positions within field bounds
def getPositionsWithinBounds(positions:List, rowMaxIndex, columnMaxIndex):
    positionsInBounds = []
    for entry in positions:
        rowEntry = entry[0]
        columnEntry = entry[1]
        # Skip position if index too low
        if(rowEntry < 0 or columnEntry < 0):
            continue
        # Skip position if index too high
        if(rowEntry > rowMaxIndex or columnEntry > columnMaxIndex):
            continue
        # Add position to Output
        positionsInBounds.append([rowEntry,columnEntry])
    return positionsInBounds

# Filters Positions contained in filterPool from original List
def filterPositions(raw:List, filterPool:List):
    FilteredList = []
    # Iterate over list
    for entry in raw:
        # filter an entry from pool
        for filter in filterPool:
            if(coordinatesAreEqual(entry,filter)):
                continue
            FilteredList.append(entry)
    # Return list without contents of filterPool
    return FilteredList

#Returns Boolean Comparison of two sets of coordinates
def coordinatesAreEqual(PositionOne:List, PositionTwo:List):
    return numpy.all(numpy.logical_and(PositionOne[0] == PositionTwo[0], PositionOne[1] == PositionTwo[1]))

# Filters Positions not contained in filterPool from original List
def filterPositionsNon(raw:List, filterPool:List):
    FilteredList = []
    # Iterate over list
    for entry in raw:
        # Filter entries not contained in pool
        for filter in filterPool:
            if(coordinatesAreEqual(entry,filter)):
                FilteredList.append(entry)
    return FilteredList

# Returns number of friendly Neighbors for any coordinate pair
def getFriendlyNeighborCount(Board:ndarray, friendlyTile, rowPos, columnPos):

    friendlyNeighbors = 0
    # Determine valid neighboring positions and all blocked positions on board
    ValidPos = getValidPositionsAroundPiece(rowPos,columnPos,Board)
    # Get Coordinates of positions that contain pieces
    NonEmpty = getNonEmptyPositions(Board)
    # Determine blocked neighboring positions
    BlockedPos = filterPositionsNon(NonEmpty, ValidPos)

    # Check if Blocked Neighbors contain friendly tile
    for entry in BlockedPos:
        tile = Board[entry[0]][entry[1]]
        if tile == friendlyTile:
            friendlyNeighbors += 1
    # Return count of friendly neighbors
    return friendlyNeighbors
    

# Gets number of winning Conditions fulfilled by placing tile at given position.
def getWinCounts(rowIndex:int, columnIndex:int, playerTile:int, board:ndarray):
    winCounter = 0
    # Evaluates wheather a horizontal win could be achieved
    if isHorizontalWin(rowIndex,columnIndex,playerTile,board):
        winCounter + 1
    # Evalutates wheather a vertical win could be achieved
    if isVerticalWin(rowIndex,columnIndex,playerTile, board):
        winCounter + 1
    # Evaluates wheather a diagonal win could be achieved
    if isDiagonalWin(rowIndex,columnIndex,playerTile, board):
        winCounter + 1    

    return winCounter

# Evaluates if move completes row of sequence of four identical tiles
def isHorizontalWin(rowIndex:int, columnIndex:int, playerTile:int, board:ndarray):
    return False

# Evaluates if move completes column of sequence of four identical tiles
def isVerticalWin(rowIndex:int, columnIndex:int, playerTile:int, board:ndarray):
    return False

# Evaluates if move completes diagonal of sequence of four identical tiles
def isDiagonalWin(rowIndex:int, columnIndex:int, playerTile:int, board:ndarray):
    return False