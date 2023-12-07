#INPUT HANDLING
inputFile = open('day4/input.txt')
inputTxt = inputFile.readlines()
inputFile.close()


#MAIN SECTION
numCards = []
for i in range(len(inputTxt)):
    numCards.append(1)


for i in range(len(inputTxt)):
    nextCard = i + 1
    line = inputTxt[i]
    cardPoints = 0
    data = line.split(':')[1].split('|')
    winners = data[0].split()
    ours = data[1].split()

    for j in range(len(winners)):
        winners[j] = int(winners[j])
    for j in range(len(ours)):
        ours[j] = int(ours[j])
        if ours[j] in winners:
            numCards[nextCard] += numCards[i]
            nextCard += 1

print(sum(numCards))