class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self,text)

#        self.message_text = text
#        self.valid_words = load_words(WORDLIST_FILENAME)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        dict4={}
        shift=0
        dict6={}
        for shift in range(0,26):
                word=Message.apply_shift(self,shift)
                dict4[shift]=word
#       print  dict4

        for key in dict4.keys():
                dict5=[]
                dict5=dict4[key].split(' ')
                incr=0
                for i in dict5:
                        if is_word(self.valid_words,i)==True:
                                incr+=1
                dict6[key]=incr

#       print dict6

        x=max(dict6.values())
        y=dict6.keys()[dict6.values().index(x)]
        for key,value in dict4.items():
                if key == y:
                        return key,value

