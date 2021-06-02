'''
Static board eval for minmax
@author Lukas Eckert
'''


from numpy import ndarray


# Evaluates Score for current board as static evaluation
def scoreBoard(board:ndarray, player:int, applyInverse:bool):
    # Use 0 as default score
    staticScore = 0

    ScoreWin = 10000
    Score3InRow = 5000
    

    return staticScore