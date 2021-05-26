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
    if(rowIndex < len(Array) and columnIndex < len(Array[rowIndex])):
        Array[rowIndex][columnIndex] = symbol
        return Array
    printErrorMsg(f"Invalid row %d or column %d index", (rowIndex,columnIndex))

def changeSymbol(row:int, col:int, Array:list, symbol):
    if(row < len(Array) and col < len(Array[row])):
        Array[row][col] = symbol
        return
    printErrorMsg(f"Invalid row %d or column %d index", (row,col))    

# Prints an array to the console.
def printArrayToConsole(Array:list):
    rowIndex = 0
    for row in Array:
        print(f"Row {rowIndex + 1} :")
        printListAsRow(row) 
        rowIndex += 1
    return
