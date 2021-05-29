'''
Test implementation of TicTacToe played on a 6x6 numpy array
'''


from typing import Counter
from arrayUtils import *
from printUtils import *

# runs a singular turn
def doTurn(brd:ndarray, turn):
    turn = turn + 1
    print(turn)
    turn = turn % 2
    print(turn)
    printArrayColors(brd)
    promptAction(turn,brd)

# prompts user for input
def promptAction(turnNr, brd:ndarray):

    column = int(input("Choose Column-Coord"))
    row = int(input("Choose Row-Coord"))

    if(turnNr == 0):
        doPlacementAction(row,column,brd,turnNr, TILE_PLAYER_RED)
    else:
        doPlacementAction(row,column,brd,turnNr,TILE_PLAYER_WHITE)
    return

# Repeats turn until successful placement of tile
def doPlacementAction(rowIndex,columnIndex,brd:ndarray,trn,Tile):
    if couldSetTile(rowIndex,columnIndex,brd,Tile):
        return
    promptAction(trn,brd)

# Checks if a win state has been reached
def checkIfWin(brd:ndarray):
    AnyWins = []
    AnyWins.append(checkIfWinRows(brd))
    AnyWins.append(checkIfWinColumns(brd))
    AnyWins.append(checkIfWinDiags(brd))

    print(AnyWins)

    for entry in AnyWins:
        if entry == True:
            doWin(brd)

# ends the program if win has been achieved
def doWin(brd:ndarray):
    global Running
    global Turn
    Running = False
    if Turn == 0:
        printYellowMsg("Player Red (2) Won")
    else:
        printYellowMsg("Player White (1) Won")
    printArrayColors(brd)

# checks for win conditions in rows
def checkIfWinRows(brd:ndarray):
    #global Board
    countSame = 0
    for rowIndex in range(brd.shape[0] - 1):
        newCount = 1
        for columnIndex in range(brd.shape[1] - 1):
            current = brd[rowIndex][columnIndex]
            next = brd[rowIndex][columnIndex + 1]
            #print(f"Current Tile: %d, Next Tile: %d" % (current,next))
            if next == current and next != TILE_EMPTY:
                newCount += 1
                #print(f"Incrementing newCount to %d" % newCount)
            if newCount > countSame:
                countSame = newCount
            #print(f"Count is %d" % countSame)
        if countSame == 4:
            return True
    return False

# checks for win conditions in columns
def checkIfWinColumns(brd:ndarray):
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
            if newCount > countSame:
                countSame = newCount
            #print(f"Count is %d" % countSame)
        if countSame == 4:
            return True
    return False

# checks for win conditions in diagonals
def checkIfWinDiags(brd:ndarray):
    if isBoardTooSmall(brd):
        return
    if(getDiagonalCount(brd) >= 4):
        return True
    return False

# evaluates the total maximum sequence of identical tiles for any diagonal line
def getDiagonalCount(brd:ndarray):
    maxLeft = getCountMaxLeftDiag(brd)
    maxRight = getCountMaxRightDiag(brd)
    print(f"maxRight{maxRight} maxLeft{maxLeft}")
    if maxLeft >= maxRight:
        return maxLeft
    return maxRight

# Evaluates the maximum sequence of identical tiles for any diagonal line runnig from top left to bottom right
def getCountMaxLeftDiag(brd:ndarray):
    # Max count found
    leftMaxCount = 1
    # Min Values
    minColumnIndex = 0
    minRowIndex = 0
    # Max Values
    maxColumnIndex = brd.shape[1] - 1
    maxRowIndex = brd.shape[0] - 1

    # loop over diagonal lines starting on y axis
    for rowStepper in range(minRowIndex,maxRowIndex):
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
            #print(f"C:{current}x{currentX}y{currentY},N:{next}x{currentX + 1}y{currentY + 1}")
            if next == current and next != TILE_EMPTY:
                # increment sequence count and maxSequence
                diagCount += 1
                #print(f"DiagCount:{diagCount}")
                if diagCount > diagCountMax:
                    diagCountMax = diagCount
        # eval max sequence in diags
        if diagCountMax > leftMaxCount:
            leftMaxCount = diagCountMax

    #printErrorMsg("Starting on Y= 0")

    # loop over remaining diagonal lines starting on x axis
    for columnStepper in range(minColumnIndex + 1,maxColumnIndex):
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
            #print(f"C:{current}x{currentX}y{currentY},N:{next}x{currentX + 1}y{currentY + 1}")
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
    return leftMaxCount


# Evaluates the maximum sequence of identical tiles for any diagonal line runnig from top right to bottom left
def getCountMaxRightDiag(brd:ndarray):
    # Max count found
    rightMaxCount = 1
    # Min Values
    minColumnIndex = 0
    minRowIndex = 0
    # Max Values
    maxColumnIndex = brd.shape[1] - 1
    maxRowIndex = brd.shape[0] - 1

    # loop over diagonal lines starting on y axis
    for rowStepper in range(maxRowIndex,minRowIndex,-1):
        #print(f"y axis stepper:{stepper}")
        diagCount = 1
        diagCountMax = 0
        # Loop through diagonal line
        for diagStepper in range(maxColumnIndex):
            #print(f"diagStepper {diagStepper}")
            # Eval if coords of tiles in board
            currentColumn = minColumnIndex + diagStepper
            currentRow = rowStepper - diagStepper
            if (currentRow - 1) < minRowIndex or (currentColumn + 1) > maxColumnIndex:
                break
            # Eval if tiles are in sequence
            current = brd[currentRow][currentColumn]
            next = brd[currentRow - 1][currentColumn + 1]
            #print(f"C:{current}x{currentX}y{currentY},N:{next}x{currentX + 1}y{currentY - 1}")
            if next == current and next != TILE_EMPTY:
                # increment sequence count and maxSequence
                diagCount += 1
                #print(f"DiagCount:{diagCount}")
                if diagCount > diagCountMax:
                    diagCountMax = diagCount
        # eval max sequence in diags
        if diagCountMax > rightMaxCount:
            rightMaxCount = diagCountMax

    #printErrorMsg("Starting on Y= 0")

    # loop over remaining diagonal lines starting on x axis
    for columnStepper in range(minColumnIndex + 1,maxColumnIndex):
        #print(f"x Axis xStepper {xStepper}")
        diagCount = 1
        diagCountMax = 0
        # Loop through diagonal line
        for diagStepper in range(maxColumnIndex):
            #print(f"diagStepper {diagStepper}")
            currentColumn = columnStepper + diagStepper
            currentRow = maxRowIndex - diagStepper
            if (currentColumn + 1) > maxColumnIndex or (currentRow - 1) < minRowIndex:
                break
            # Eval if tiles are in sequence
            current = brd[currentRow][currentColumn]
            next = brd[currentRow - 1][currentColumn + 1]
            #print(f"C:{current}x{currentX}y{currentY},N:{next}x{currentX + 1}y{currentY + 1}")
            if next == current and next != TILE_EMPTY:
                # increment sequence count and maxSequence
                diagCount += 1
                #print(f"DiagCount:{diagCount}")
                if diagCount > diagCountMax:
                    diagCountMax = diagCount
        # eval max sequence in diags
        if diagCountMax > rightMaxCount:
            rightMaxCount = diagCountMax

    # end function, return max count found
    return rightMaxCount


# Checks if the Board is too Small for diagonal win 
def isBoardTooSmall(Board:ndarray):
    if((Board.shape[0] - 1 )< 4 or (Board.shape[1] - 1)< 4):
        return True
    return False


'''

# global vars
Running = True
Board = createEmptyBoard(6,6)
Turn:int = 0
TurnCount:int = 0
WinningPlayer = 0

# main loop
while (Running):
    doTurn(Board)
    checkIfWin(Board)

'''

# does some stats
def doStatisticsForTurn(winnerIndex, turn):
    turn + 1
    WinningPlayer = winnerIndex

