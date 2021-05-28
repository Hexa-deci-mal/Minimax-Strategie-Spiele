from arrayUtils import getNonEmptyPositions
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

# Filters Positions not contained in filterPool from original List
def filterPositionsNon(raw:List, filterPool:List):
    FilteredList = []
    for entry in raw:
        if(entry in filterPool):
            FilteredList.append(entry)
    return FilteredList

# Returns number of friendly Neighbors for any coordinate pair
def getFriendlyNeighborCount(Board:ndarray, friendlyTile, yPos, xPos):
    friendlyNeighbors = 0
    # Determine valid neighboring positions and all blocked positions on board
    ValidPos = getValidPositionsAroundPiece(xPos,yPos,Board)
    print("Valids:")
    print(ValidPos)
    NonEmpty = getNonEmptyPositions(Board)
    print("Blocked")
    print(NonEmpty)
    # Determine blocked neighboring positions
    BlockedPos = filterPositionsNon(NonEmpty, ValidPos)
    print("Blocked Valid")
    print(BlockedPos)
    # Check if Blocked Neighbors contain friendly tile
    for entry in BlockedPos:
        tile = Board[entry[0]][entry[1]]
        print(f"Tile:{tile} at x:{entry[0]} y:{entry[1]}")
        if tile == friendlyTile:
            friendlyNeighbors += 1
    # Return count of friendly neighbors
    return friendlyNeighbors
    