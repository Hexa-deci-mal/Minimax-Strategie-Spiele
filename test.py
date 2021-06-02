'''
ndarrays
'''

from arrayUtils import *
from printUtils import *
from ticTacToe import *



diagTest = createEmptyBoard(6,6)
setIfEmpty(3,0,diagTest,1)
setIfEmpty(4,1,diagTest,1)
setIfEmpty(5,2,diagTest,1)

setIfEmpty(0,0,diagTest,1)
setIfEmpty(1,1,diagTest,1)
setIfEmpty(2,2,diagTest,1)
setIfEmpty(3,3,diagTest,1)
setIfEmpty(4,4,diagTest,1)
setIfEmpty(5,5,diagTest,1)

setIfEmpty(0,2,diagTest,1)
setIfEmpty(1,3,diagTest,1)
setIfEmpty(2,4,diagTest,1)
setIfEmpty(3,5,diagTest,1)



diagTest2 = createEmptyBoard(6,6)
setIfEmpty(0,1,diagTest2,2)
setIfEmpty(1,0,diagTest2,2)

setIfEmpty(0,3,diagTest2,2)
setIfEmpty(1,2,diagTest2,2)
setIfEmpty(2,1,diagTest2,2)
setIfEmpty(3,0,diagTest2,2)
2
setIfEmpty(1,5,diagTest2,2)
setIfEmpty(2,4,diagTest2,2)
setIfEmpty(3,3,diagTest2,2)
setIfEmpty(4,2,diagTest2,2)
setIfEmpty(5,1,diagTest2,2)
2
setIfEmpty(5,5,diagTest2,2)



diagTest3 = createEmptyBoard(6,6)
setIfEmpty(0,1,diagTest3,1)
setIfEmpty(2,3,diagTest3,1)
setIfEmpty(3,4,diagTest3,1)
setIfEmpty(4,5,diagTest3,1)

setIfEmpty(3,0,diagTest3,1)
setIfEmpty(4,1,diagTest3,1)
setIfEmpty(5,2,diagTest3,1)

setIfEmpty(1,5,diagTest3,1)

setIfEmpty(0,3,diagTest3,2)
setIfEmpty(1,2,diagTest3,2)
setIfEmpty(2,1,diagTest3,2)

setIfEmpty(2,4,diagTest3,2)
setIfEmpty(3,3,diagTest3,2)
setIfEmpty(4,2,diagTest3,2)
setIfEmpty(5,1,diagTest3,2)


print()
printArrayColors(diagTest)
print()
print(f"LeftCountMax {getCountMaxLeftDiag(diagTest)}")
print(f"RightCountMax {getCountMaxRightDiag(diagTest)}")



print()
printArrayColors(diagTest2)
print()
print(f"LeftCountMax {getCountMaxLeftDiag(diagTest2)}")
print(f"RightCountMax {getCountMaxRightDiag(diagTest2)}")



print()
printArrayColors(diagTest3)
print()
print(f"LeftCountMax {getCountMaxLeftDiag(diagTest3)}")
print(f"RightCountMax {getCountMaxRightDiag(diagTest3)}")
