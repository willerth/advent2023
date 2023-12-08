#INPUT HANDLING
inputFile = open('day05/input.txt')
inputSections = inputFile.read().split(':')[1:]

seeds = inputSections[0].split()[:-2]
for i in range(len(seeds)):
    seeds[i] = int(seeds[i])

mapRangeArrays = []
maps = []
results = []

for i in range(1, len(inputSections)):
    mapRangeArrays.append([])
    section = inputSections[i]
    sectionLines = section.strip().split('\n')

    for j in range(len(sectionLines)):
        if(sectionLines[j] == ''): break
        mapRangeArrays[i - 1].append(sectionLines[j])

    #break

maps = ['SOIL','FERT','WATER','LIGHT','TEMPERATURE','HUMID','LOC']
for seed in seeds:
    for mapRangeArray in mapRangeArrays:
        for mapRange in mapRangeArray:
            mapRange = mapRange.split()
            rangeStart = int(mapRange[1])
            rangeLength = int(mapRange[2])

            if(seed >= rangeStart and seed < rangeStart + rangeLength):
                seed = (seed - rangeStart) + int(mapRange[0])
                break

        #print(f'{maps[count]} : {seed}')

    results.append(seed)

print(sorted(results))
exit()

for i in range(len(mapRangeArrays)):
    mapRangeArray = mapRangeArrays[i]
    maps.append({})
    for mapRange in mapRangeArray:
        numberForm = mapRange.split()
        mapStart = int(numberForm[1])
        mapEnd = int(numberForm[0])
        mapRange = int(numberForm[2])
        for j in range(mapRange):
            print(f'we are on {i}, {j}')
            maps[i][mapStart + j] = mapEnd + j

#MAIN SECTION
for seed in seeds:
    for map in maps:
        seed = map[seed] if seed in map.keys() else seed
    
    results.append(seed)

results.sort()
print(results)
        
    