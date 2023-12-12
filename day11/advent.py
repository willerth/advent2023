from util import *

#inputFile = open('day11/example.txt')
inputFile = open('day11/input.txt')
inputTxt = inputFile.readlines()
inputFile.close()

universe = []

for i in range(len(inputTxt)):
    universe.append(inputTxt[i].strip())


EMPTY_ROWS = findEmptyRows(universe)
EMPTY_COLUMNS = findEmptyRows(transposed(universe))

numColumns = len(universe[0])

galaxies = []
sum = 0



for i in range(len(universe)):
    for j in range(numColumns):
        if(universe[i][j] == '#'):
            galaxies.append([i,j])


for i in range(len(galaxies)):
    origin = galaxies[i]
    for j in range(i + 1, len(galaxies)):
        terminal = galaxies[j]
        sum += calculateDistance(origin, terminal, EMPTY_ROWS, EMPTY_COLUMNS, 1_000_000)


print(sum)