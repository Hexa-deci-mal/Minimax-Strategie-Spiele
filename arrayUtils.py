'''
Implementation of various utility functions for handling 2D arrays used within the project.
@author Lukas Eckert
'''

from listUtils import *

TILE_EMPTY = 'TILE_EMPTY'
TILE_CHECKERS_WHITE = 'TILE_WHITE_CHECKERS'
TILE_CHECKERS_RED = 'TILE_RED_CHECKERS'

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
    print("Invalid row or column index")


# Prints an array to the console. Array is broken up into individual rows.
def printArrayToConsole(Array:list):
    rowIndex = 0
    for row in Array:
        print(f"Row {rowIndex + 1} :")
        print(f"{Array[rowIndex][0]} {Array[rowIndex][1]} {Array[rowIndex][2]} {Array[rowIndex][3]} {Array[rowIndex][4]} {Array[rowIndex][5]}")
        rowIndex += 1
    return


