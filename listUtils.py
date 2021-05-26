'''
Provides various quality of life utilities for using lists
'''

# Creates an uniform list which is (size) symbols long containing only the given (symbol).
def getUniformList(size:int, symbol):
    uniList = []
    for x in range(size):
        uniList.append(symbol)
    return uniList
