'''
Utilities that provide easy console output options. Intended use is for creating test outputs and for providing easy to use error messages.
'''

# Prints a message to console using red color.
def printErrorMsg(msg):
    print(f'\033[91m{msg}\033[0m')

# Prints an invalid index error
def errorInvalidIndex(row:int,col:int,Array:list):
    actRow = len(Array)
    actCol = 0
    for rows in Array:
        if(len(rows) - 1 > actCol):
            actCol = len(rows) - 1
    if(row > actRow):
        printErrorMsg("Invalid row %d index for row size %d" % (row,actRow))
        return
    if(col > actCol):
        printErrorMsg("Invalid column %d index for column size %d" % (col,actCol))
        return