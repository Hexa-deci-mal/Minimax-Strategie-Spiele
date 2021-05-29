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
    if(checkBoardBounds(rowIndex,columnIndex,Board) and Board[rowIndex,columnIndex] == TILE_EMPTY):
        Board[rowIndex,columnIndex] = symbol
        return True
    return False
    

# Returns the tile stored in the numpy array at the specified position rowIndex = Y, columnIndex = X
def getTileFromPosition(rowIndex:int, columnIndex:int, Board:ndarray):
    if(checkBoardBounds(rowIndex,columnIndex,Board)):
        return Board[rowIndex][columnIndex]

# Checks if index is within valid index bounds row = Y, column = X
def checkBoardBounds(row:int, column:int, Board:ndarray):
    return row < Board.shape[0] and column < Board.shape[1] and row >= 0 and column >= 0

'''
FAULTY FUNCTION, DONT USE

# Returns the positions of pieces
def getPositionsOfPieces(Board:ndarray, piece:int):
    NonZero = nonzero(Board == piece)
    for entry in NonZero:
        for val in entry:
            val -=1
    return NonZero
'''

# Returns all positions that are not empty
def getNonEmptyPositions(Board:ndarray):
    positions = []
    #print(nonzero(Board))
    columnIndex = nonzero(Board)[1]
    rowIndex = nonzero(Board)[0]
    for cc in range(rowIndex.size):
        positions.append([rowIndex[cc],columnIndex[cc]])
    return positions

'''
BB = createEmptyBoard(3,3)
setIfEmpty(1,0,BB,2)
setIfEmpty(1,1,BB,3)
#printArrayColors(BB)
for entry in getNonEmptyPositions(BB):
    print(entry)

'''