def hangman(secretWord):

    print 'Welcome to the game, Hangman!'
    x=len(secretWord)
    print 'I am thinking of a word that is %d letters long' %(x)
    print '----------------------------------------------'
    mistakeMade=8
    lettersGuessed=[]


    while mistakeMade>0:
        print 'You have %d guesses left' %(mistakeMade)

        print 'Available Letters: ',getAvailableLetters(lettersGuessed)

        guess = (raw_input('Please guess a letter: ')).lower()


        if guess in secretWord:

                if guess  not in getAvailableLetters(lettersGuessed):
                        print "Oops! You've already guessed that letter: ",getGuessedWord(secretWord, lettersGuessed)
                        print ' ----------------------------------------------------'


                else:
                        lettersGuessed.append(guess)
                        print 'Good guess: ',getGuessedWord(secretWord, lettersGuessed)
                        print ' ----------------------------------------------------'
                        if isWordGuessed(secretWord,lettersGuessed):
                                print 'Congratulations, you won!'
                                return None


        else:
                 if guess  not in getAvailableLetters(lettersGuessed):
                        print "Oops! You've already guessed that letter: ",getGuessedWord(secretWord, lettersGuessed)
                        print ' ----------------------------------------------------'


                 else:
                        lettersGuessed.append(guess)
                        print 'Oops! That letter is not in my word:  ',getGuessedWord(secretWord, lettersGuessed)
                        print '--------------------------------------------'
                        mistakeMade -= 1

                        if mistakeMade == 0:
                                print'Sorry, you ran out of guesses  word was %s' %(secretWord)
                                return None

