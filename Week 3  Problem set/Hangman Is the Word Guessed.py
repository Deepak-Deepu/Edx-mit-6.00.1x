def isWordGuessed(secretWord,lettersGuessed):
        count =0
        for i in secretWord:
                if i in lettersGuessed:
                        count += 1 

        return(len(secretWord)==count)
