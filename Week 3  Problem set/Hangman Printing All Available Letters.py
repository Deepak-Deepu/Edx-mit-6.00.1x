def getAvailableLetters(lettersGuessed):
        qwe=''
        import string
        w=string.ascii_lowercase
        for i in w: 
                if i not in lettersGuessed:
                        qwe += i
        return qwe

