'''
Implementation of various utility functions for handling 2D arrays used within the project.
@author Lukas Eckert
'''

import numpy
from numpy import *

# Empty Tile
TILE_EMPTY = 0

# White Player Tile
TILE_PLAYER_WHITE = 1

# Red Player Tile
TILE_PLAYER_RED = 2

# Creates a new numpy array containing only 0 values. Rows = Y, Columns = X
def createEmptyBoard(rows:int, columns:int):
    Board = numpy.zeros((rows, columns))
    return Board

# Places a tile at a specific coordinate set within the numpy array. rowIndex = Y, columnIndex = X
def setIfEmpty(rowIndex:int, columnIndex:int, Board:ndarray, symbol:int):
    if(checkBoardBounds(rowIndex,columnIndex,Board) and Board[rowIndex,columnIndex] == TILE_EMPTY):
        Board[rowIndex,columnIndex] = symbol

# Tries setting a tile at a specific coordinate set within the numpy array. rowIndex = Y, columnIndex = 16
# Returns Boolean value indicating success
def couldSetTile(rowIndex:int, columnIndex:int, Board:ndarray, symbol:int):
    if checkBoardBounds(rowIndex,columnIndex,Board):
        if getTileFromPosition(rowIndex,columnIndex, Board) == TILE_EMPTY:
            Board[rowIndex,columnIndex] = symbol
            return True
    return False
    
# Clones the board
def cloneBoard(board:ndarray):

    return board.copy()

# Returns the tile stored in the numpy array at the specified position rowIndex = Y, columnIndex = X
def getTileFromPosition(rowIndex:int, columnIndex:int, Board:ndarray):
    comp = checkBoardBounds(rowIndex,columnIndex,Board)
    if comp:
        return Board[rowIndex][columnIndex]

# Checks if index is within valid index bounds row = Y, column = X
def checkBoardBounds(row:int, column:int, Board:ndarray):
    return row < Board.shape[0] and column < Board.shape[1] and row >= 0 and column >= 0


# Returns all positions that are not empty
def getNonEmptyPositions(Board:ndarray):
    positions = []
    columnIndex = nonzero(Board)[1]
    rowIndex = nonzero(Board)[0]
    for cc in range(rowIndex.size):
        positions.append([rowIndex[cc],columnIndex[cc]])
    return positions

'''

# Returns all empty positions from a given Board
def getEmptyPositions(Board:ndarray):
    # Get all positions
    positions = getAllPositionsOnBoard(Board)
    # Get filled positions
    filledPositions = getNonEmptyPositions(Board)

    # Filter filled positions from all positions
    emptyPositions = filterPositions(positions,filledPositions)
    return emptyPositions

# Get all Positions [indexRow,indexColumn] from a given board
def getAllPositionsOnBoard(Board:ndarray):
    allPositions = []
    # crawl through board and add all positions
    for rowCrawler in range(Board.shape[0] - 1):
        for columnCrawler in range(Board.shape[1] - 1):
            allPositions.append([rowCrawler,columnCrawler])
    
    return allPositions

'''

'''
BB = createEmptyBoard(3,3)
setIfEmpty(1,0,BB,2)
setIfEmpty(1,1,BB,3)
#printArrayColors(BB)
for entry in getNonEmptyPositions(BB):
    print(entry)

'''