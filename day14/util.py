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

def shiftPlatformNorth(arr):
    maxColIdx = len(arr[0])
    for i in range(maxColIdx):
        shiftColumnNorth(arr, i)


def calculateLoad(arr):
    sum = 0
    for i in range(len(arr)):
        multiplier = len(arr) - i
        for j in range(len(arr[i])):
            if(arr[i][j]) == 'O': sum += multiplier

    return sum