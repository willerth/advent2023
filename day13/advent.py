from util import *

#inputFile = open('day13/example.txt')
inputFile = open('day13/input.txt')
inputBlocks = inputFile.read().split('\n\n')
inputFile.close()

sum = 0
counter = 1

for block in inputBlocks:
    block = block.splitlines()
    transposedBlock = transposed(block)

    horizontalReflectionLine = findHorizontalReflectionLine(block, 1)
    verticalReflectionLine = findHorizontalReflectionLine(transposedBlock, 1)

    if(horizontalReflectionLine == verticalReflectionLine):
        print(counter)
        print(f'{horizontalReflectionLine} | {verticalReflectionLine}')
        print('\n'.join(block))
    counter += 1

    if horizontalReflectionLine != -1: sum += 100 * horizontalReflectionLine
    if verticalReflectionLine != -1: sum += verticalReflectionLine


print(sum)