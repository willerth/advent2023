def shiftColumnNorth(arr, colIdx):
    northernmostFreeSpace = 0
    for i in range(len(arr)):
        char = arr[i][colIdx]
        if char == 'O':
            arr[i][colIdx] = '.'
            arr[northernmostFreeSpace][colIdx] = 'O'
            northernmostFreeSpace += 1
        if char == '#':
            northernmostFreeSpace = i + 1


def shiftRowWest(arr, rowIdx):
    westernmostFreeSpace = 0
    for i in range(len(arr[0])):
        char = arr[rowIdx][i]
        if char == 'O':
            arr[rowIdx][i] = '.'
            arr[rowIdx][westernmostFreeSpace] = 'O'
            westernmostFreeSpace += 1
        if char == '#':
            westernmostFreeSpace = i + 1


#Flip it and reverse it
def shiftColumnSouth(arr, colIdx):
    southernmostFreeSpace = len(arr) - 1
    for i in range(len(arr) - 1, -1, -1):
        char = arr[i][colIdx]
        if char == 'O':
            arr[i][colIdx] = '.'
            arr[southernmostFreeSpace][colIdx] = 'O'
            southernmostFreeSpace -= 1
        if char == '#':
            southernmostFreeSpace = i - 1


def shiftRowEast(arr, rowIdx):
    westernmostFreeSpace = len(arr[0]) - 1
    for i in range(len(arr[0]) - 1, -1, -1):
        char = arr[rowIdx][i]
        if char == 'O':
            arr[rowIdx][i] = '.'
            arr[rowIdx][westernmostFreeSpace] = 'O'
            westernmostFreeSpace -= 1
        if char == '#':
            westernmostFreeSpace = i - 1




def shiftPlatformNorth(arr):
    maxColIdx = len(arr[0])
    for i in range(maxColIdx):
        shiftColumnNorth(arr, i)

def shiftPlatformWest(arr):
    maxRowIdx = len(arr)
    for i in range(maxRowIdx):
        shiftRowWest(arr, i)

def shiftPlatformSouth(arr):
    maxColIdx = len(arr[0])
    for i in range(maxColIdx):
        shiftColumnSouth(arr, i)

def shiftPlatformEast(arr):
    maxRowIdx = len(arr)
    for i in range(maxRowIdx):
        shiftRowEast(arr, i)



def spinCycle(arr):
    functions = [
        shiftPlatformNorth,
        shiftPlatformWest,
        shiftPlatformSouth,
        shiftPlatformEast
    ]
    for function in functions:
        function(arr)



def calculateLoad(arr):
    sum = 0
    for i in range(len(arr)):
        multiplier = len(arr) - i
        for j in range(len(arr[i])):
            if(arr[i][j]) == 'O': sum += multiplier

    return sum