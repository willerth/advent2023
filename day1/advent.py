coordsFile = open('day1/coords.txt')
rawTxt = coordsFile.readlines()
coordsFile.close()

sum = 0

numsinTxt = [
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine'
]

for line in rawTxt:
    i = 0
    j = len(line) - 1

    while(not line[i].isdigit()):
        i+=1
    firstDigit = int(line[i])

    while(not line[j].isdigit()):
        j-=1
    secondDigit = int(line[j])

    for k in range(0, 10):
        searchedDigit = numsinTxt[k]
        if(searchedDigit in line):
            idx = line.index(searchedDigit)
            ridx = line.rindex(searchedDigit)
            if(idx < i):
                firstDigit = k
                i = idx
            if(ridx > j):
                secondDigit = k
                j = ridx
    
    sum += 10 * firstDigit + secondDigit
    

print(sum)