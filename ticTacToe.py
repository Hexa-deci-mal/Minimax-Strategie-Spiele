'''
Test implementation of TicTacToe played on a 6x6 numpy array
'''


from typing import Counter
from arrayUtils import *
from printUtils import *

# runs a singular turn
def doTurn(brd:ndarray):
    global Turn
    Turn = Turn + 1
    print(Turn)
    Turn = Turn % 2
    print(Turn)
    printArrayColors(brd)
    promptAction(Turn,brd)

# prompts user for input
def promptAction(turnNr, brd:ndarray):

    x = int(input("Choose X-Coord"))
    y = int(input("Choose Y-Coord"))

    if(turnNr == 0):
        doPlacementAction(y,x,brd,turnNr, TILE_PLAYER_RED)
    else:
        doPlacementAction(y,x,brd,turnNr,TILE_PLAYER_WHITE)
    return

# Repeats turn until successful placement of tile
def doPlacementAction(y,x,brd:ndarray,trn,Tile):
    if couldSetTile(y,x,brd,Tile):
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
    for y in range(brd.shape[0] - 1):
        newCount = 1
        for x in range(brd.shape[1] - 1):
            current = brd[y][x]
            next = brd[y][x + 1]
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
    for x in range(brd.shape[1] - 1):
        newCount = 1
        for y in range(brd.shape[0] - 1):
            current = brd[y][x]
            next = brd[y + 1][x]
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
    minX = 0
    minY = 0
    # Max Values
    maxX = brd.shape[1] - 1
    maxY = brd.shape[0] - 1

    # loop over diagonal lines starting on y axis
    for stepper in range(minY,maxY):
        #print(f"y axis stepper:{stepper}")
        diagCount = 1
        diagCountMax = 0
        # Loop through diagonal line
        for diagStepper in range(maxX - stepper):
            #print(f"diagStepper {diagStepper}")
            # Eval if coords of tiles in board
            currentX = stepper + diagStepper
            currentY = minX + diagStepper
            if (currentY + 1) > maxY or (currentX + 1) > maxX:
                break
            # Eval if tiles are in sequence
            current = brd[currentY][currentX]
            next = brd[currentY + 1][currentX + 1]
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
    for xStepper in range(minX + 1,maxX):
        #print(f"x Axis xStepper {xStepper}")
        diagCount = 1
        diagCountMax = 0
        # Loop through diagonal line
        for diagStepper in range(maxX):
            #print(f"diagStepper {diagStepper}")
            currentX = xStepper + diagStepper
            currentY = minY + diagStepper
            if (currentX + 1) > maxX or (currentY + 1) > maxY:
                break
            # Eval if tiles are in sequence
            current = brd[currentY][currentX]
            next = brd[currentY + 1][currentX + 1]
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
    minX = 0
    minY = 0
    # Max Values
    maxX = brd.shape[1] - 1
    maxY = brd.shape[0] - 1

    # loop over diagonal lines starting on y axis
    for stepper in range(maxY,minY,-1):
        #print(f"y axis stepper:{stepper}")
        diagCount = 1
        diagCountMax = 0
        # Loop through diagonal line
        for diagStepper in range(maxX):
            #print(f"diagStepper {diagStepper}")
            # Eval if coords of tiles in board
            currentX = minX + diagStepper
            currentY = stepper - diagStepper
            if (currentY - 1) < minY or (currentX + 1) > maxX:
                break
            # Eval if tiles are in sequence
            current = brd[currentY][currentX]
            next = brd[currentY - 1][currentX + 1]
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
    for xStepper in range(minX + 1,maxX):
        #print(f"x Axis xStepper {xStepper}")
        diagCount = 1
        diagCountMax = 0
        # Loop through diagonal line
        for diagStepper in range(maxX):
            #print(f"diagStepper {diagStepper}")
            currentX = xStepper + diagStepper
            currentY = maxY - diagStepper
            if (currentX + 1) > maxX or (currentY - 1) < minY:
                break
            # Eval if tiles are in sequence
            current = brd[currentY][currentX]
            next = brd[currentY - 1][currentX + 1]
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

'''

# Evaluates the Highest Nummber of identical non zero entries
def getDiagHighest(yStart,xStart,brd:ndarray):
    Count = 0
    if yStart >= 0:
        Count = getDiagHighestPreZero(yStart,xStart,brd)
    else:
        Count = getDiagHighestPostZero(yStart,xStart,brd)
    
    return Count

# Evaluates the Highest Nummber of identical non zero entries within a diagonal line for range yMax to y=0
def getDiagHighestPreZero(yStart,xStart,brd:ndarray):
    stepper  = 0
    count = 1
    highestCountCycle = 0
    for c in range(yStart,brd.shape[0] - 2):
        #print(f"Running eval on current:{c},{xStart + stepper} and next:{c + 1},{xStart + stepper + 1}")
        current = brd[c][xStart + stepper]
        next = brd[c + 1][xStart + stepper + 1]
        if next == current and next != TILE_EMPTY:
            print("Increment Count")
            count + 1
        else:
            if count > highestCountCycle:
                print("Increment Max")
                highestCountCycle = count
            count = 1
        stepper + 1
    return highestCountCycle

# Evaluates the Highest Nummber of identical non zero entries within a diagonal line for range y = 0 to xMax
def getDiagHighestPostZero(xStart,yStart,brd:ndarray):
    stepper  = 0
    count = 1
    highestCountCycle = 0
    for c in range(xStart,brd.shape[1] - 2):
        current = brd[yStart + stepper][c]
        next = brd[yStart + stepper][c + 1]
        if next == current and next != TILE_EMPTY:
            count + 1
        else:
            if count > highestCountCycle:
                highestCountCycle = count
            count = 1
        stepper + 1
    return highestCountCycle

'''

# Checks if the Board is too Small for diagonal win 
def isBoardTooSmall(Board:ndarray):
    if((Board.shape[0] - 1 )< 4 or (Board.shape[1] - 1)< 4):
        return True
    return False



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

# does some stats
def doStatisticsForTurn(winnerIndex):
    global TurnCount
    global WinningPlayer
    TurnCount + 1
    WinningPlayer = winnerIndex


