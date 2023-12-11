from util import *
BID_INDEX = 5

#inputFile = open('day07/example.txt')
inputFile = open('day07/input.txt')
inputTxt = inputFile.readlines()
inputFile.close()

FACES_TO_NUMBERS = {
    'T' : 10,
    'J' : 0,
    'Q' : 12,
    'K' : 13,
    'A' : 14
}


hands = []
bids = []
for line in inputTxt:
    line = line.split()
    hands.append(line[0])
    bids.append(line[1])

for i in range(len(hands)):
    hand = list(hands[i])
    for j in range(len(hand)):
        card = hand[j]
        if card in FACES_TO_NUMBERS.keys():
            hand[j] = FACES_TO_NUMBERS[card]
        else:
            hand[j] = int(hand[j])

    hand.append(bids[i])

    cardCounts = {}
    
    for card in hand:
        cardCounts[card] = 1 if card not in cardCounts.keys() else cardCounts[card] + 1


    categories[determineRank(cardCounts)].append(hand)

sum = 0
rank = 1
for category in categories.keys():
    for hand in sorted(categories[category]):
        #print(hand)
        sum += rank * int(hand[BID_INDEX])
        rank += 1
        #print(sum)

print(sum)
