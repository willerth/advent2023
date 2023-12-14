from util import *

NUM_CYCLES = 1000000000

inputFile = open('day14/example.txt')
#inputFile = open('day14/input.txt')
inputTxt = inputFile.readlines()
inputFile.close()

platform = []
for line in inputTxt:
    line = line.strip()
    row = []
    for char in line.strip():
        row.append(char)
    platform.append(row)

for i in range(NUM_CYCLES):
    spinCycle(platform)

print(calculateLoad(platform))


#exit()
#Just seeing what the platform looks like

for row in platform:
    print(''.join(row))