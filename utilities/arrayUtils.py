'''
Implementation of various utility functions for handling 2D arrays used within the project.
@author Lukas Eckert
'''
from utilities.listUtils import *
from utilities.printUtils import *

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

# Prints an array to the console. Array is broken up into individual rows for display purposes.
def printArrayToConsole(Array:list):
    rowIndex = 0
    for row in Array:
        print(f"Row {rowIndex + 1} :")
        print(f"{Array[rowIndex][0]} {Array[rowIndex][1]} {Array[rowIndex][2]} {Array[rowIndex][3]} {Array[rowIndex][4]} {Array[rowIndex][5]}")
        rowIndex += 1
    return
