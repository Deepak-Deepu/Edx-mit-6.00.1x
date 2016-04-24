def updateHand(hand,word):

        hand1=hand.copy()
        for i in word:
                hand1[i]=hand1[i]-1
        return hand1

