inputFile = open('day08/input.txt')
inputTxt = inputFile.readlines()
inputFile.close()

directionsArray = []
map = {}

firstLine = inputTxt[0].strip()
for char in firstLine:
    directionsArray.append(0 if char == 'L' else 1)

for line in inputTxt[2:]:
    line = line.split('=')
    origin = line[0].strip()

    destinations = line[1].strip()[1:-1]
    destinations = destinations.split(', ')

    map[origin] = destinations


currentLocation = 'AAA'
directionsIndex = 0
count = 0
while(currentLocation != 'ZZZ'):
    direction = directionsArray[directionsIndex]
    directionsIndex = (directionsIndex + 1) % len(directionsArray)
    currentLocation = map[currentLocation][direction]

    count += 1

print(count)