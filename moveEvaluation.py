from typing import List
from numpy import *

# Gets valid positions around piece
def getValidPositionsAroundPiece(xPiece,yPiece,board:ndarray):
    return getPositionsWithinBounds(getPositionsAroundPiece(xPiece,yPiece),board.shape[0] - 1,board.shape[1] - 1)

# Returns all positions surrounding a piece
def getPositionsAroundPiece(xPiece, yPiece):
    PosAround = []
    PosAround.extend(getHorizontalPos(xPiece,yPiece))
    PosAround.extend(getVerticalPos(xPiece,yPiece))
    PosAround.extend(getDiagonalPos(xPiece,yPiece))
    return PosAround

# returns possible horizontal coords
def getHorizontalPos(xPos,yPos):
    xMin = xPos - 1
    xMax = xPos + 1
    return [[xMin,yPos],[xMax,yPos]]

# returns possible Vertical coords
def getVerticalPos(xPos,yPos):
    yMin = yPos - 1
    yMax = yPos + 1
    return [[xPos,yMin],[xPos,yMax]]

# Returns possible Diagonal coords
def getDiagonalPos(xPos,yPos):
    yMin = yPos - 1
    yMax = yPos + 1
    xMin = xPos - 1
    xMax = xPos + 1
    return [[xMin,yMax],[xMin,yMin],[xMax,yMin],[xMax,yMax]]

# Returns positions within field bounds
def getPositionsWithinBounds(positions:List, xFieldMaxIndex, yFieldMaxIndex):
    positionsInBounds = []
    for entry in positions:
        xEntry = entry[0]
        yEntry = entry[1]
        # Skip position if index too low
        if(xEntry < 0 or yEntry < 0):
            continue
        # Skip position if index too high
        if(xEntry > xFieldMaxIndex or yEntry > yFieldMaxIndex):
            continue
        # Add position to Output
        positionsInBounds.append([xEntry,yEntry])
    return positionsInBounds

# Filters Positions contained in filterPool from original List
def filterPositions(raw:List, filterPool:List):
    FilteredList = []
    for entry in raw:
        if(entry in filterPool):
            continue
        FilteredList.append(entry)
    return FilteredList

