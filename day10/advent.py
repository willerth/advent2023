from util import *

for direction in startDirections:
    x = STARTING_LOCATION[0] + direction[0]
    y = STARTING_LOCATION[1] + direction[1]
    try:
        foundChar = pureMap[x][y]
        if(foundChar == '.' or direction not in directions[foundChar].keys()): continue
        q.put([direction, [x,y], foundChar])
        numberedMap[x][y] = 1
    except:
        pass

maxDist = 1

while(not q.empty()):
    datum = q.get()
    #print(datum)

    originDirection = datum[0]
    location = datum[1]
    pipe = datum[2]
    continuedDirection = directions[pipe][originDirection]
    
    originX = location[0]
    originY = location[1]
    x = originX + continuedDirection[0]
    y = originY + continuedDirection[1]

    foundChar = pureMap[x][y]
    if(foundChar not in directions.keys() or continuedDirection not in directions[foundChar].keys()): continue
    q.put([continuedDirection, [x,y], foundChar])
    pureMap[originX][originY] = '.'
    numberedMap[x][y] = numberedMap[originX][originY] + 1
    if(maxDist < numberedMap[x][y]) : maxDist = numberedMap[x][y]

print(maxDist)

exit()

for row in numberedMap:
    for char in row:
        print(char, end='')
    print()

exit()

for row in pureMap:
    for char in row:
        print(char, end='')
    print()

