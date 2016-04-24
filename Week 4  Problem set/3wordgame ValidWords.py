def isValidWord(word,hand,wordList):
    
    if word not in wordList:
        return False

    result = True
    handcopy = hand.copy()
    resulthand = getFrequencyDict(word)

    try:
        for key in resulthand.keys():
            handcopy[key] -= resulthand[key]
            if handcopy.get(key, 0) < 0:
                return False
    except KeyError as e:
        return False

    return result
