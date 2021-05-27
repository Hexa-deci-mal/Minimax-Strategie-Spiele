'''
Utilities that provide easy console output options. Intended use is for creating test outputs and for providing easy to use error messages.
'''

# Prints a message to console using red color.
from arrayUtils import TILE_PLAYER_RED, TILE_PLAYER_WHITE
from numpy import ndarray
from numpy.core.fromnumeric import shape


# Print red error msg
def printErrorMsg(msg):
    print(f'\033[91m{msg}\033[0m')

# Print yellow text
def printYellowMsg(msg):
    print(f'\033[93m{msg}\033[0m')

# Print Array in nice
def printArrayColors(Array:ndarray):
    for y in range(Array.shape[0]):
        String = ""
        for x in range(Array.shape[1]):
            String += (f"[%s]" % formatForColor(Array[y][x]))
        print(String)

# Formats String Color to match player color
def formatForColor(msg:int):
    msgStr = f'%d' % msg
    if msg == TILE_PLAYER_RED:
        return f'\033[91m{msg}\033[0m'
    if msg == TILE_PLAYER_WHITE:
        return f'\033[96m{msg}\033[0m'
    return msgStr
