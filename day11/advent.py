from util import *

#inputFile = open('day11/example.txt')
inputFile = open('day11/input.txt')
inputTxt = inputFile.readlines()
inputFile.close()

universe = transposed(expand(transposed(expand(inputTxt))))

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
        xDist = abs(origin[0] - terminal[0])
        yDist = abs(origin[1] - terminal[1])
        sum += xDist + yDist

    #break

print(sum)