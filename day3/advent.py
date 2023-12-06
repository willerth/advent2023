import math


#INPUT HANDLING
inputFile = open('day3/input.txt')
inputTxt = inputFile.readlines()
inputFile.close()


#MAIN SECTION
sum = 0
rowIdx = 0
symbolLocations = []
numberLocations = []


for rowIdx in range(len(inputTxt)):
    line = inputTxt[rowIdx].strip()

    symbolLocations.append([])
    numberLocations.append([])
    colIdx = 0


    while(colIdx < len(line)):
        currentNumber = 0
        while(colIdx < len(line) and line[colIdx].isdigit()):
            currentNumber *= 10
            currentNumber += int(line[colIdx])
            colIdx += 1
        
        if(currentNumber != 0):
            numberLocations[rowIdx].append((colIdx, currentNumber))
            continue

        if(line[colIdx] != '.'):
            symbolLocations[rowIdx].append(colIdx)


        colIdx += 1


for i in range(len(inputTxt)):
    print(f'\n\nROW {i}')
    minRowToCheck = 0 if i == 0 else i - 1
    maxRowToCheck = len(inputTxt) - 1 if i == len(inputTxt) - 1 else i + 1

    numbersInRow = numberLocations[i]
    for number in numbersInRow:
        isPartNumber = False
        column = number[0]
        value = number[1]
        numDigits = math.ceil(math.log(value, 10))

        minColToCheck = column - numDigits - 1
        maxColToCheck = column
        for row in range(minRowToCheck, maxRowToCheck + 1):
            for col in range(minColToCheck, maxColToCheck + 1):
                if col in symbolLocations[row]:
                    isPartNumber = True

        print(f'{value} is {"NOT " if not isPartNumber else ""}a part number')
        sum += value * isPartNumber


print(sum)
    