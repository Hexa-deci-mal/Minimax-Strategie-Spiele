from ticTacToe import getDiagonalCount
from arrayUtils import *
from numpy import *
from printUtils import *
from moveEvaluation import *


'''
GameBoard = createEmptyBoard(6,6)

print(GameBoard)

setIfEmpty(2,2,GameBoard,TILE_PLAYER_RED)

print(GameBoard)

print(getTileFromPosition(2,2,GameBoard))
'''


testBoard = createEmptyBoard(4,4)
setIfEmpty(1,1,testBoard,2)
setIfEmpty(0,1,testBoard,1)
setIfEmpty(2,1,testBoard,2)
setIfEmpty(2,2,testBoard,2)
setIfEmpty(3,3,testBoard,1)
setIfEmpty(3,0,testBoard,2)
setIfEmpty(1,2,testBoard,1)
setIfEmpty(0,3,testBoard,2)
printArrayColors(testBoard)
#print(getPositionsOfPieces(testBoard, 2))
PositionArray = getNonEmptyPositions(testBoard)
PosList = []
for pos in PositionArray:
   PosList.append([pos[0],pos[1]])
#print(PosList)

print(getFriendlyNeighborCount(testBoard,2,2,1))

#print(getValidPositionsAroundPiece(1,1,testBoard))
#print(getValidPositionsAroundPiece(0,0,testBoard))
#print(getValidPositionsAroundPiece(3,3,testBoard))

#print(getValidPositionsAroundPiece(1,3,testBoard))
#print(filterPositions(getValidPositionsAroundPiece(1,3,testBoard),PosList))

#print(getDiagonalCount(testBoard))

#BB = createEmptyBoard(3,3)
#setIfEmpty(1,0,BB,2)
#setIfEmpty(1,1,BB,3)
#printArrayColors(BB)
#for entry in getNonEmptyPositions(BB):
#    print(entry)