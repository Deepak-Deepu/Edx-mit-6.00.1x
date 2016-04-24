def playGame(wordList):
    # TO DO... <-- Remove this comment when you code this function
#    print "playGame not yet implemented." # <-- Remove this when you code this function
    user=0
    comp=0
    while True:
            word=raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
            if word == 'r':
                if word =='r' and user == 0:
                        print'You have not played a hand yet. Please play a new hand first!'
                elif word =='r' and comp == 0:
                        print'You have not played a hand yet. Please play a new hand first!'
                elif word == 'r' and user !=0 and comp !=0:
                        while True:
                                word=raw_input('\nEnter u to have yourself play, c to have the computer play: ')
                                if word == 'u':
                                        playHand(hand, wordList,HAND_SIZE)
                                        user += 1
                                        comp += 1
                                        break
                                elif word == 'c':
                                        compPlayHand(hand, wordList,HAND_SIZE)
                                        comp += 1
                                        user += 1
                                        break
                                elif word== 'e':
                                        break
                                else:
                                        print 'Invalid comment'



            elif word=='n':
                while True:
                        word=raw_input('\nEnter u to have yourself play, c to have the computer play: ')
                        if word == 'u':
                                hand = dealHand(HAND_SIZE)
                                playHand(hand, wordList,HAND_SIZE)
                                user += 1
                                comp += 1
                                break
                        elif word == 'c':
                                hand = dealHand(HAND_SIZE)
                                compPlayHand(hand, wordList,HAND_SIZE)
                                comp += 1
                                user += 1
                                break
                        elif word== 'e':
                                break
                        else:
                                print 'Invalid command'
            
            elif word == 'e':
                break
            else:
                print 'Invalid comment'

