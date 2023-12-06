#CONSTANT DECLARATION
MAXIMUMS = {
    'red' : 12,
    'green' : 13,
    'blue' : 14
}


#INPUT HANDLING
inputFile = open('day2/input.txt')
inputTxt = inputFile.readlines()
inputFile.close()


#MAIN SECTION
possibleGames = 0
sumOfPowers = 0

for i in range(len(inputTxt)):
    minimums = {
        'red' : 0,
        'blue' : 0,
        'green' : 0
    }

    isPossible = True
    line = inputTxt[i].strip()
    data = line.split(':')[1].strip()               #variable data contains info for every pull
    samples = data.split(';')
    for sample in samples:                          #variable sample contains info for an individual pull
        atoms = sample.split(',')
        for atom in atoms:                          #variable atom contains how many cubes of a single color are in the elf's hand at one time (this is a wild comment to read out of context)
            number = int(atom.split()[0])
            color = atom.split()[1]
            if(number > MAXIMUMS[color]):
                isPossible = False
            if(number > minimums[color]):
                minimums[color] = number

    #update sums
    #pt 1
    possibleGames += (i + 1) * isPossible

    #pt 2
    power = 1
    for multiplier in minimums.values():
        power *= multiplier
    sumOfPowers += power

print(possibleGames)
print(sumOfPowers)