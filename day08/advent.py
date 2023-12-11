from math import lcm

#inputFile = open('day08/example.txt')
inputFile = open('day08/input.txt')
inputTxt = inputFile.readlines()
inputFile.close()

directionsArray = []
currentLocations = []
map = {}

firstLine = inputTxt[0].strip()
for char in firstLine:
    directionsArray.append(0 if char == 'L' else 1)

for line in inputTxt[2:]:
    line = line.split('=')
    origin = line[0].strip()

    if(origin[-1]) == 'A':
        currentLocations.append(origin)

    destinations = line[1].strip()[1:-1]
    destinations = destinations.split(', ')

    map[origin] = destinations

pathLengths = []

for location in currentLocations:
    directionsIndex = 0
    pathLength = 0
    while(location[-1] != 'Z'):
        pathLength += 1
        direction = directionsArray[directionsIndex]
        directionsIndex = (directionsIndex + 1) % len(directionsArray)
        location = map[location][direction]

    pathLengths.append(pathLength)

print(pathLengths)
print(lcm(*pathLengths))