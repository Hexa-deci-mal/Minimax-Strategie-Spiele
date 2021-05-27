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

# Creates a new numpy array containing only 0 values.
def createEmptyBoard(rows:int, columns:int):
    Board = numpy.zeros((rows, columns))
    return Board

# Places a tile at a specific coordinate set within the numpy array.
def setIfEmpty(rowIndex:int, columnIndex:int, Board:ndarray, symbol:int):
    if(checkBoardBounds(rowIndex,columnIndex,Board)):
        Board[rowIndex,columnIndex] = symbol

# Returns the tile stored in the numpy array at the specified position
def getTileFromPosition(rowIndex:int, columnIndex:int, Board:ndarray):
    if(checkBoardBounds(rowIndex,columnIndex,Board)):
        return Board[rowIndex][columnIndex]

# Checks if index is within valid index bounds
def checkBoardBounds(row:int, column:int, Board:ndarray):
    return row < Board.shape[0] and column < Board.shape[1]