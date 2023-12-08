#INPUT HANDLING
inputFile = open('day05/exampleInput.txt')
inputSections = inputFile.read().split(':')[1:]

parsedSeeds = inputSections[0].split()[:-2]
seeds = []
for i in range(0, len(parsedSeeds), 2):
    rangeStart = int(parsedSeeds[i])
    rangeLen = int(parsedSeeds[i + 1])
    for j in range(rangeLen):
        seeds.append(rangeStart + j)

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
    