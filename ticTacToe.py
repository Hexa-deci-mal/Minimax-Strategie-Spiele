'''
Test implementation of TicTacToe played on a 6x6 numpy array
@author Lukas Eckert
'''


from tkinter.constants import FALSE
from typing import Counter
from arrayUtils import *
from printUtils import *

# Executes Turn with input given


def doAutoTurn(brd: ndarray, turn, running, rowIn, colIn):

    if not running:
        return [brd, turn, running]
    #print("AutoTurn")
    runningCache = running
    brdCache = brd
    turnCache = turn + 1
    # print(turnCache)
    turnCache = turnCache % 2
    # print(turnCache)
    #printArrayColors(brd)
    #print(turn)
    #print(running)
    #print(rowIn)
    #print(colIn)
    autoRes = doAutoAction(turnCache, brdCache, runningCache, rowIn, colIn)
    #print(f"AutoRes {autoRes}")
    if(not autoRes[1]):
        #print("Reset Turn")
        turnCache = turn
    return [brdCache, turnCache, autoRes[0]]

# runs a singular turn


def doTurn(brd: ndarray, turn, running):
    runningCache = running
    brdCache = brd
    turnCache = turn + 1
    # print(turnCache)
    turnCache = turnCache % 2
    # print(turnCache)
    #printArrayColors(brd)
    runningCache = promptAction(turnCache, brdCache, runningCache)
    return [brdCache, turnCache, runningCache]

# prompts user for input


def promptAction(turnNr, brd: ndarray, running):

    column = int(input("Choose Column-Coord"))
    row = int(input("Choose Row-Coord"))

    if(turnNr == 0):
        doPlacementAction(row, column, brd, turnNr, TILE_PLAYER_RED)
    else:
        doPlacementAction(row, column, brd, turnNr, TILE_PLAYER_WHITE)
    return not checkIfWin(brd, turnNr, running)

# Executes given TurnAction


def doAutoAction(turnNr:int, brd: ndarray, running, rowCall:int, columnCall:int):
    #print("Auto-Action")
    executed = False
    if(turnNr == 0):
        executed = doAutoPlacementAction(
            rowCall, columnCall, brd, turnNr, TILE_PLAYER_RED)
    else:
        executed = doAutoPlacementAction(
            rowCall, columnCall, brd, turnNr, TILE_PLAYER_WHITE)

    return [not checkIfWin(brd, turnNr, running), executed]


# Tries to execute turn automatically
def doAutoPlacementAction(rowIndex:int, columnIndex:int, brd: ndarray, trn, Tile):
    if couldSetTile(rowIndex, columnIndex, brd, Tile):
        return True
    return False

# Repeats turn until successful placement of tile


def doPlacementAction(rowIndex, columnIndex, brd: ndarray, trn, Tile):
    if couldSetTile(rowIndex, columnIndex, brd, Tile):
        return
    promptAction(trn, brd, True)

# Checks if a win state has been reached


def checkIfWin(brd: ndarray, trn, running):
    AnyWins = []
    AnyWins.append(checkIfWinRows(brd))
    AnyWins.append(checkIfWinColumns(brd))
    AnyWins.append(checkIfWinDiags(brd))
    #print(AnyWins)
    for entry in AnyWins:
        if entry == True:
            doWin(brd, trn)
            return True
    return False

# ends the program if win has been achieved


def doWin(brd: ndarray, trn):
    if trn == 0:
        printYellowMsg("Player Red (2) Won")
    else:
        printYellowMsg("Player White (1) Won")
    printArrayColors(brd)

# checks for win conditions in rows


def checkIfWinRows(brd: ndarray):
    #global Board
    countSame = 0
    for rowIndex in range(brd.shape[0] - 1):
        newCount = 1
        for columnIndex in range(brd.shape[1] - 1):
            current = brd[rowIndex][columnIndex]
            next = brd[rowIndex][columnIndex + 1]
            #print(f"Current Tile: %d, Next Tile: %d" % (current, next))
            if next == current and next != TILE_EMPTY:
                newCount += 1
                #print(f"Incrementing newCount to %d" % newCount)
            else:
                newCount = 1
            if newCount > countSame:
                countSame = newCount
            #print(f"Count is %d" % countSame)
        if countSame == 4:
            return True
    return False

# checks for win conditions in columns


def checkIfWinColumns(brd: ndarray):
    #global Board
    countSame = 0
    for columnIndex in range(brd.shape[1] - 1):
        newCount = 1
        for rowIndex in range(brd.shape[0] - 1):
            current = brd[rowIndex][columnIndex]
            next = brd[rowIndex + 1][columnIndex]
            #print(f"Current Tile: %d, Next Tile: %d" % (current,next))
            if next == current and next != TILE_EMPTY:
                newCount += 1
                #print(f"Incrementing newCount to %d" % newCount)
            else:
                newCount = 1
            if newCount > countSame:
                countSame = newCount
            #print(f"Count is %d" % countSame)
        if countSame == 4:
            return True
    return False

# checks for win conditions in diagonals


def checkIfWinDiags(brd: ndarray):
    if isBoardTooSmall(brd):
        return False
    if(getDiagonalCount(brd) >= 4):
        return True
    return False

# evaluates the total maximum sequence of identical tiles for any diagonal line


def getDiagonalCount(brd: ndarray):
    maxLeft = getCountMaxLeftDiag(brd)
    maxRight = getCountMaxRightDiag(brd)
    #print(f"maxRight{maxRight} maxLeft{maxLeft}")
    if maxLeft >= maxRight:
        return maxLeft
    return maxRight

# Evaluates the maximum sequence of identical tiles for any diagonal line runnig from top left to bottom right


def getCountMaxLeftDiag(brd: ndarray):

    #printErrorMsg("lt2rb")
    # Max count found
    leftMaxCount = 1
    # Min Values
    minColumnIndex = 0
    minRowIndex = 0
    # Max Values
    maxColumnIndex = brd.shape[1] - 1
    maxRowIndex = brd.shape[0] - 1

    # loop over diagonal lines starting on y axis
    for rowStepper in range(minRowIndex, maxRowIndex):
        #print(f"y axis stepper:{stepper}")
        diagCount = 1
        diagCountMax = 0
        # Loop through diagonal line
        for diagStepper in range(maxColumnIndex - rowStepper):
            #print(f"diagStepper {diagStepper}")
            # Eval if coords of tiles in board
            currentColumn = rowStepper + diagStepper
            currentRow = minColumnIndex + diagStepper
            if (currentRow + 1) > maxRowIndex or (currentColumn + 1) > maxColumnIndex:
                break
            # Eval if tiles are in sequence
            current = brd[currentRow][currentColumn]
            next = brd[currentRow + 1][currentColumn + 1]
            #print(f"Cur:{current} row:{currentRow} col:{currentColumn}, Nex:{next} row:{currentRow + 1} col:{currentColumn + 1}")
            if next == current and next != TILE_EMPTY:
                # increment sequence count and maxSequence
                diagCount += 1
                #print(f"DiagCount:{diagCount}")
                if diagCount > diagCountMax:
                    diagCountMax = diagCount
        # eval max sequence in diags
        if diagCountMax > leftMaxCount:
            leftMaxCount = diagCountMax

    #printErrorMsg("column loop lt2rb")

    # loop over remaining diagonal lines starting on x axis
    for columnStepper in range(minColumnIndex + 1, maxColumnIndex):
        #print(f"x Axis xStepper {xStepper}")
        diagCount = 1
        diagCountMax = 0
        # Loop through diagonal line
        for diagStepper in range(maxColumnIndex):
            #print(f"diagStepper {diagStepper}")
            currentColumn = columnStepper + diagStepper
            currentRow = maxRowIndex + diagStepper
            if (currentColumn + 1) > maxColumnIndex or (currentRow + 1) > maxRowIndex:
                break
            # Eval if tiles are in sequence
            current = brd[currentRow][currentColumn]
            next = brd[currentRow + 1][currentColumn + 1]
            #print(f"C:{current} r{currentRow} c{currentColumn},N:{next} r{currentRow + 1} c{currentColumn + 1}")
            if next == current and next != TILE_EMPTY:
                # increment sequence count and maxSequence
                diagCount += 1
                #print(f"DiagCount:{diagCount}")
                if diagCount > diagCountMax:
                    diagCountMax = diagCount
        # eval max sequence in diags
        if diagCountMax > leftMaxCount:
            leftMaxCount = diagCountMax

    # end function, return max count found
    #print(f"Left Max {leftMaxCount}")
    return leftMaxCount


# Evaluates the maximum sequence of identical tiles for any diagonal line runnig from top right to bottom left
def getCountMaxRightDiag(brd: ndarray):

    #printErrorMsg("tr2bl")

    # Max count found
    rightMaxCount = 1
    # Min Values
    minColumnIndex = 0
    minRowIndex = 0
    # Max Values
    maxColumnIndex = brd.shape[1] - 1
    maxRowIndex = brd.shape[0] - 1

    # loop over diagonal lines starting on x axis
    for colStepper in range(maxColumnIndex, minColumnIndex, -1):
        #print(f"y axis stepper:{stepper}")
        diagCount = 1
        diagCountMax = 0
        # Loop through diagonal line
        for diagStepper in range(maxRowIndex):
            #print(f"diagStepper {diagStepper}")
            # Eval if coords of tiles in board
            currentColumn = colStepper - diagStepper
            currentRow = minRowIndex + diagStepper
            if (currentRow + 1) > minRowIndex or (currentColumn - 1) < maxColumnIndex:
                break
            # Eval if tiles are in sequence
            current = brd[currentRow][currentColumn]
            next = brd[currentRow + 1][currentColumn - 1]
            #print(f"C:{current} r{currentRow} c{currentColumn},N:{next} r{currentRow + 1} c{currentColumn - 1}")
            if next == current and next != TILE_EMPTY:
                # increment sequence count and maxSequence
                diagCount += 1
                # print(f"DiagCount:{diagCount}")
                if diagCount > diagCountMax:
                    diagCountMax = diagCount
        # eval max sequence in diags
        if diagCountMax > rightMaxCount:
            rightMaxCount = diagCountMax

    #printErrorMsg("Starting on row= 1")

    # loop over remaining diagonal lines starting on y axis
    for rwStepper in range(1,maxRowIndex):
        #print(f"x Axis xStepper {xStepper}")
        diagCount = 1
        diagCountMax = 0
        # Loop through diagonal line
        for clStepper in range(maxColumnIndex + 1):
            #print(f"diagStepper {diagStepper}")
            currentColumn = maxColumnIndex - clStepper
            currentRow = minRowIndex + clStepper
            if (currentColumn - 1) < minColumnIndex or (currentRow + 1) > maxRowIndex:
                break
            # Eval if tiles are in sequence
            current = brd[currentRow][currentColumn]
            next = brd[currentRow + 1][currentColumn - 1]
            #print(f"C:{current} x{currentRow} y{currentColumn},N:{next} x{currentRow + 1}y {currentColumn - 1}")
            if next == current and next != TILE_EMPTY:
                # increment sequence count and maxSequence
                diagCount += 1
                # print(f"DiagCount:{diagCount}")
                if diagCount > diagCountMax:
                    diagCountMax = diagCount
        # eval max sequence in diags
        if diagCountMax > rightMaxCount:
            rightMaxCount = diagCountMax

    #print(f"rightmaxcount {rightMaxCount}")
    # end function, return max count found
    return rightMaxCount


# Checks if the Board is too Small for diagonal win
def isBoardTooSmall(Board: ndarray):
    if((Board.shape[0] - 1) < 4 or (Board.shape[1] - 1) < 4):
        return True
    return False


'''
# global vars
MainRunning = True
MainBoard  = createEmptyBoard(6,6)
MainTurn = 0
TurnCount:int = 0
WinningPlayer = 0

# main loop
while (MainRunning):
    TurnResult = doTurn(MainBoard, MainTurn, MainRunning)
    MainBoard = TurnResult[0]
    MainTurn = TurnResult[1]
    MainRunning = TurnResult[2]

'''

# does some stats


def doStatisticsForTurn(winnerIndex, turn):
    turn + 1
    WinningPlayer = winnerIndex
