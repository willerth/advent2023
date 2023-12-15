#just reusing the transposing code from day 11
def transposed(block):
    transposedBlock = []
    numColumns = len(block[0])
    for j in range(numColumns):
        newString = []
        for i in range(len(block)):
            newString.append(block[i][j])
        transposedBlock.append(''.join(newString))
    return transposedBlock


def isHorizontalReflectionLine(arr, lineIdx):
    topIdx = lineIdx
    bottomIdx = lineIdx - 1
    while(topIdx < len(arr) and bottomIdx >= 0):
        if(arr[topIdx] != arr[bottomIdx]): return False

        topIdx += 1
        bottomIdx -= 1
    return True


def findHorizontalReflectionLine(arr):
    for i in range(1, len(arr)):
        if(isHorizontalReflectionLine(arr, i)) : return i
    return -1