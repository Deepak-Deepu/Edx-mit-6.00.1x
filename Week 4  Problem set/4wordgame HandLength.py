def calculateHandlen(hand):
    count=0
    for i in hand.keys():
        count += hand[i]
    return count
