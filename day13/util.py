def transposed(block):
    transposedBlock = []
    numColumns = len(block[0])
    for j in range(numColumns):
        newString = []
        for i in range(len(block)):
            newString.append(block[i][j])
        transposedBlock.append(''.join(newString))
    return transposedBlock

def stringDifference(stringA, stringB):
    sum = 0
    for i in range(len(stringA)):
        if stringA[i] != stringB[i]: sum += 1
    return sum


def isHorizontalReflectionLine(arr, lineIdx, numSmudges = 0):
    topIdx = lineIdx
    bottomIdx = lineIdx - 1
    totalDifferences = 0
    while(topIdx < len(arr) and bottomIdx >= 0):
        totalDifferences += stringDifference(arr[topIdx], arr[bottomIdx])

        topIdx += 1
        bottomIdx -= 1
    return totalDifferences == numSmudges


def findHorizontalReflectionLine(arr, numSmudges = 0):
    for i in range(1, len(arr)):
        if(isHorizontalReflectionLine(arr, i, numSmudges)) : return i
    return -1