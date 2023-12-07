#INPUT HANDLING
inputFile = open('day4/input.txt')
inputTxt = inputFile.readlines()
inputFile.close()


#MAIN SECTION
totalPoints = 0

for line in inputTxt:
    cardPoints = 0
    data = line.split(':')[1].split('|')
    winners = data[0].split()
    ours = data[1].split()

    for i in range(len(winners)):
        winners[i] = int(winners[i])
    for i in range(len(ours)):
        ours[i] = int(ours[i])
        if ours[i] in winners:
            cardPoints = (1 if cardPoints == 0 else cardPoints * 2)

    totalPoints += cardPoints

print(totalPoints)