from queue import Queue
from dataclasses import dataclass


#SETUP
inputFile = open('day10/example.txt')
#inputFile = open('day10/input.txt')
inputText = inputFile.readlines()
inputFile.close()

startDirections = (
    (0,1),
    (0,-1),
    (1,0),
    (-1,0)
)

directions = {}

directions['|'] = {
    (1,0) : (1,0),
    (-1, 0) : (-1, 0)
}

directions['-'] = {
    (0,1) : (0,1),
    (0,-1) : (0,-1)
}

directions['L'] = {
    (1,0) : (0,1),
    (0,-1) : (-1,0)
}

directions['J'] = {
    (1,0) : (0,-1),
    (0,1) : (-1,0)
}

directions['7'] = {
    (-1,0) : (0,-1),
    (0,1) : (1,0)
}

directions['F'] = {
    (-1,0) : (0,1),
    (0,-1) : (1, 0)
}

STARTING_LOCATION = []
q = Queue()

NUM_ROWS = 0
pureMap = []
numberedMap = []
for line in inputText:
    colNumber = 0
    pureMap.append([])
    numberedMap.append([])
    for character in line:
        if character == 'S': STARTING_LOCATION = [NUM_ROWS, colNumber]
        if(character) == '\n': continue
        pureMap[NUM_ROWS].append(character)
        numberedMap[NUM_ROWS].append(character)
        colNumber += 1

    NUM_ROWS += 1

numberedMap[STARTING_LOCATION[0]][STARTING_LOCATION[1]] = 0
