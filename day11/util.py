def transposed(list):
    numColumns = len(list[0])
    result = []
    for i in range(numColumns):
        result.append([])
        for j in range(len(list)):
            result[i].append(list[j][i])
        
        result[i] = ''.join(result[i])

    return result


def findEmptyRows(list):
    result = []
    for i in range(len(list)):
        if'#' not in list[i]:
            result.append(i)
    return result


def calculateDistance(galaxyA, galaxyB, emptyRows, emptyColumns, expansionCoefficient=2):
    ax = galaxyA[1]
    bx = galaxyB[1]
    ay = galaxyA[0]
    by = galaxyB[0]

    distance = 0

    xIncrement = 1 if ax < bx else -1
    yIncrement = 1 if ay < by else -1


    for y in range(ay, by, yIncrement):
        distance += expansionCoefficient if y in emptyRows else 1

    for x in range(ax, bx, xIncrement):
        distance += expansionCoefficient if x in emptyColumns else 1
    return distance


def expand(universe, multiplier=2):
    result = []
    for line in universe:
        result.append(line.strip())
        if '#' not in line:
            for i in range(1, multiplier):
                result.append(line.strip())
    
    return result

