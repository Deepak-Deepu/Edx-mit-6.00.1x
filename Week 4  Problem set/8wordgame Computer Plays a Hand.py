def compChooseWord(hand, wordList, n):
    TotalScore=0
    BestWord='None'
    BestScore=0
    for word in wordList:
        if (isValidWord(word,hand,wordList))==True:
                TotalScore=0
                TotalScore += (getWordScore(word,n))
                if TotalScore > BestScore:
                        BestScore = TotalScore
                        BestWord = word
    return BestWord

def compPlayHand(hand, wordList, n):
    Totalscore=0
#    hand =dealHand(n)
    while True:
        print"current Hand:",
        displayHand(hand)
        word=compChooseWord(hand, wordList, n)
        if word !='None':
                Totalscore += (getWordScore(word,n))
                print '"' + str(word)+'"' + " earned " + str(getWordScore(word,n)) + " points." + " Total: " + str(Totalscore) + " points\n"
                hand= updateHand(hand,word)
                if calculateHandlen(hand) == 0:
                        print "Total score: " + str(Totalscore) + " points."
                        break
        else:
                print "Total score: " + str(Totalscore) + " points."
                break

