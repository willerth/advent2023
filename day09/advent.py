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
    
    nextInSeq = -1
    for j in range(len(data) - 1, 0, -1):
        lastIdx = len(data[j]) - 1
        lastDiff = data[j][lastIdx]
        nextInSeq = data[j - 1][lastIdx] + lastDiff
        data[j - 1].append(nextInSeq)
        #print(lastIdx)
    

    result += nextInSeq



print(result)