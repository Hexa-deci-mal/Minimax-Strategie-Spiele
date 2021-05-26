'''
This concept aims to explore possible implementations for a 2d array data structure. This 2d array is meant to provide the application with a unified interface to transfer relevant data between
different sub-components of the software.

All code within this concept should be considered work in progress. Extreme changes may occur at any time without prior notice.
@author: Lukas Eckert
'''

from arrayUtils import *

'''
The datastructure is required to store 2D positional data for board game pieces placed on a static 6x6 game board. The datastructure needs to provide the following infos in a concise manner:
    - x-coordinate of the figure
    - y-coordinate of the figure
    - type of the figure


An 2 dimensional array can be used to easily define the position of it's contents via it's index. The array can also be iterated through easily to perform any data manipulation tasks.
'''


GameArray = [[0,1,2,3,4,5],[0,1,2,3,4,5],[0,1,2,3,4,5],[0,1,2,3,4,5],[0,1,2,3,4,5],[0,1,2,3,4,5]]

print(GameArray[0])

print(GameArray[4][5])

rowIndex = 0
for row in GameArray:
    rowIndex += 1
    print(f"Start row {rowIndex}")
    for column in row:
        print(column)

'''
The content of each position within the array can be directly accessed using it's row and column index. The content itself can represent a specific type of data.
'''

Field = createEmptyArray(6,6)

printArrayToConsole(Field)

Field = fillArrayPosition(0,0,Field,'A')
Field = fillArrayPosition(1,1,Field,'R')
Field = fillArrayPosition(2,2,Field,'R')
Field = fillArrayPosition(3,3,Field,'A')
Field = fillArrayPosition(4,4,Field,'Y')
Field = fillArrayPosition(5,5,Field,'S')

printArrayToConsole(Field)

'''
Users are encouraged to only use provided global variables as array contents. This will prevent accidental typos.
Index out of Bounds errors are avoided using provided utility functions. Errors will be printed to console and no changes will be made to the array
'''

GlobalArrayTest = createEmptyArray(4,4)
printArrayToConsole(GlobalArrayTest)
changeSymbol(5,2,GlobalArrayTest,'CHANKE')
printArrayToConsole(GlobalArrayTest)

'''
The content of a specific row and column coordinate can be retrieved using a getter function
'''

changeSymbol(2,2,GlobalArrayTest,TILE_PLAYER_RED)
printArrayToConsole(GlobalArrayTest)
print(getSymbolFromPosition(2,2,GlobalArrayTest))
