def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
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

    print BestWord

