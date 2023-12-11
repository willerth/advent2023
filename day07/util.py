CARD_RANKS = [
    '1','2','3','4','5','6','7','8','9','T','J','Q','K','A'
]

categories = {
    'HIGH_CARD' : [],
    'ONE_PAIR' : [],
    'TWO_PAIR' : [],
    'THREE_OF_A_KIND' : [],
    'FULL_HOUSE' : [],
    'FOUR_OF_A_KIND' : [],
    'FIVE_OF_A_KIND' : []
}

def index_in_card_ranks(card):
    return(CARD_RANKS.index(card))





def determineRank(cardCounts):
    if 5 in cardCounts.values():      return('FIVE_OF_A_KIND')
    elif 4 in cardCounts.values():    return('FOUR_OF_A_KIND')
    elif 3 in cardCounts.values():
        if 2 in cardCounts.values():  return('FULL_HOUSE')
        else:                       return('THREE_OF_A_KIND')
    elif 2 in cardCounts.values():
        if list(cardCounts.values()).count(2) == 2: return('TWO_PAIR')
        else:
            return('ONE_PAIR')
    else:
        return('HIGH_CARD')

#testing = ['KK3','K44']
#testing = sorted(testing, key=index_in_card_ranks)
#print(testing)