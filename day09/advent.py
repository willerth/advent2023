#inputFile = open('day09/example.txt')
inputFile = open('day09/input.txt')
inputTxt = inputFile.readlines()
inputFile.close()

result = 0

for line in inputTxt:
    line = line.split()
    for i in range(len(line)):
        line[i] = int(line[i])

    data = [line]
    allZeroes = False

    i = 0
    while(not allZeroes):
        allZeroes = True
        newData = []
        formerSequence = data[i]
        for j in range(1, len(formerSequence)):
            difference = formerSequence[j] - formerSequence[j-1]
            if(difference != 0):
                allZeroes = False
            newData.append(difference)
        
        data.append(newData)

        i+=1
    
    newLeftMost = 0
    print(data)
    for j in range(len(data) - 1, -1, -1):
        lastDiff = data[j][0]
        data[j - 1].insert(0, data[j - 1][0] - lastDiff)
        #nextInSeq = data[j - 1][lastIdx] + lastDiff
        #data[j - 1].append(nextInSeq)
        
    print(data)
    
    print()
    result += data[0][0]



print(result)