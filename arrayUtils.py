'''
Implementation of various utility functions for handling 2D arrays used within the project.
@author Lukas Eckert
'''
from listUtils import *
from printUtils import *

# Global variables used to define array contents. 
TILE_EMPTY = 'TILE_EMPTY'
TILE_PLAYER_WHITE = 'TILE_PLAYER_WHITE'
TILE_PLAYER_RED = 'TILE_PLAYER_RED'

# Creates a new empty array containing only empty tile values.
def createEmptyArray(rows, columns):
    EmptyArray = []
    for x in range(rows):
        EmptyArray.append(getUniformList(columns,TILE_EMPTY))
    return EmptyArray

# Changes a symbol at a specific position within the array.
def fillArrayPosition(rowIndex:int, columnIndex:int, Array:list, symbol):
    if(checkArrayIndexValidity(rowIndex,columnIndex,Array)):
        Array[rowIndex][columnIndex] = symbol
        return Array
    errorInvalidIndex(rowIndex,columnIndex,Array)

# Sets a new symbol at the desired position
def changeSymbol(row:int, col:int, Array:list, symbol):
    if(checkArrayIndexValidity(row,col,Array)):
        Array[row][col] = symbol
        return
    errorInvalidIndex(row,col,Array)

# Prints an array to the console.
def printArrayToConsole(Array:list):
    rowIndex = 0
    for row in Array:
        print(f"Row {rowIndex + 1} :")
        printListAsRow(row) 
        rowIndex += 1

# Returns the symbol stored in the array at the specified position
def getSymbolFromPosition(row:int, column:int, Array:list):
    if(checkArrayIndexValidity(row,column,Array)):
        return Array[row][column]
    errorInvalidIndex(row,column)


# Checks if index is within valid index bounds
def checkArrayIndexValidity(row:int, column:int, Array:list):
    return row < len(Array) and column < len(Array[row])