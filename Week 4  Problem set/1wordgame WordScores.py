def getWordScore(word, n):
        add=0
        if(len(word) == n):
                for i in word:
                        if i in SCRABBLE_LETTER_VALUES.keys():
                                add=SCRABBLE_LETTER_VALUES[i]+add
                
                return(len(word)*add+50)

        else:
                for i in word:
                        if i in SCRABBLE_LETTER_VALUES.keys():
                                add = SCRABBLE_LETTER_VALUES[i]+add
                assert(len(word))>=0
                return(len(word)*add)

