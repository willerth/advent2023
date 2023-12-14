from util import *

#inputFile = open('day14/example.txt')
inputFile = open('day14/input.txt')
inputTxt = inputFile.readlines()
inputFile.close()

platform = []
for line in inputTxt:
    line = line.strip()
    row = []
    for char in line.strip():
        row.append(char)
    platform.append(row)

shiftPlatformNorth(platform)
print(calculateLoad(platform))
