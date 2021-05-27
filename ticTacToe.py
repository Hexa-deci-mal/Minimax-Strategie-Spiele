'''
Test implementation of TicTacToe played on a 6x6 numpy array
'''


from arrayUtils import *
from printUtils import *

# runs a singular turn
def doTurn():
    global Turn
    Turn = Turn + 1
    print(Turn)
    Turn = Turn % 2
    print(Turn)
    print(Board)
    promptAction()

# prompts user for input
def promptAction():
    global Turn

    x = int(input("Choose X-Coord"))
    y = int(input("Choose Y-Coord"))

    if(Turn == 0):
        setIfEmpty(y,x,Board, TILE_PLAYER_RED)
    else:
        setIfEmpty(y,x,Board,TILE_PLAYER_WHITE)
    return

# Checks if a win state has been reached
def checkIfWin():
    AnyWins = []
    AnyWins.append(checkIfWinRows())
    AnyWins.append(checkIfWinColumns())
    AnyWins.append(checkIfWinDiags())

    print(AnyWins)

    for entry in AnyWins:
        if entry == True:
            doWin()

# ends the program if win has been achieved
def doWin():
    global Running
    global Turn
    global Board
    Running = False
    if Turn == 0:
        printYellowMsg("Player Red (2) Won")
    else:
        printYellowMsg("Player White (1) Won")
    printArrayColors(Board)

# checks for win conditions in rows
def checkIfWinRows():
    global Board
    countSame = 0
    for y in range(Board.shape[0] - 1):
        newCount = 1
        for x in range(Board.shape[1] - 1):
            current = Board[y][x]
            next = Board[y][x + 1]
            #print(f"Current Tile: %d, Next Tile: %d" % (current,next))
            if next == current and next != 0:
                newCount += 1
                #print(f"Incrementing newCount to %d" % newCount)
            if newCount > countSame:
                countSame = newCount
            #print(f"Count is %d" % countSame)
        if countSame == 4:
            return True
    return False


# checks for win conditions in columns
def checkIfWinColumns():
    global Board
    countSame = 0
    for x in range(Board.shape[1] - 1):
        newCount = 1
        for y in range(Board.shape[0] - 1):
            current = Board[y][x]
            next = Board[y + 1][x]
            #print(f"Current Tile: %d, Next Tile: %d" % (current,next))
            if next == current and next != 0:
                newCount += 1
                #print(f"Incrementing newCount to %d" % newCount)
            if newCount > countSame:
                countSame = newCount
            #print(f"Count is %d" % countSame)
        if countSame == 4:
            return True
    return False

# checks for win conditions in diagonals
def checkIfWinDiags():
    return False

# global vars
Running = True
Board = createEmptyBoard(6,6)
Turn:int = 0

# main loop
while (Running):
    doTurn()
    checkIfWin()
