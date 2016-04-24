def getGuessedWord(secretWord,lettersGuessed):
        qwe=''
        for i in secretWord:
                if i  not in lettersGuessed:
                                qwe=qwe+'_'
                else:
                        qwe += i

        return qwe

