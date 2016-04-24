class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]

    def build_shift_dict(self, shift):

        map_dict={0:('A','a'),1:('B','b'),2:('C','c'),3:('D','d'),4:('E','e'),
               5:('F','f'),6:('G','g'),7:('H','h'),8:('I','i'),9:('J','j'),10:('K','k'),
              11:('L','l'),12:('M','m'),13:('N','n'),14:('O','o'),15:('P','p'),
                16:('Q','q'),17:('R','r'),18:('S','s'),19:('T','t'),20:('U','u'),
                21:('V','v'),22:('W','w'),23:('X','x'),24:('Y','y'),25:('Z','z')}


        shift_dict={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,
                    'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25,
                    'a':26,'b':27,'c':28,'d':29,'e':30,'f':31,'g':32,'h':33,'i':34,'j':35,'k':36,'l':37,'m':38,
                    'n':39,'o':40,'p':41,'q':42,'r':43,'s':44,'t':45,'u':46,'v':47,'w':48,'x':49,'y':50,'z':51}


        shift_dict1=shift_dict.copy()
        for i in shift_dict1.keys():
                shift_dict1[i]=shift_dict1[i]+shift
#       print shift_dict1

        j=0
        k=0
        map_result={}
        map_result=shift_dict1.copy()
        for i in shift_dict1.values():
                if i%26 in map_dict.keys():
                        if (shift_dict1.keys()[j]).islower()==True:
                                k=i%26
                                map_result[shift_dict1.keys()[j]]=map_dict[k][1]
                                j+=1
                        else:
                                k=i%26
                                map_result[shift_dict1.keys()[j]]=map_dict[k][0]
                                j+=1

        return map_result

    def apply_shift(self, shift):

        pass #delete this line and replace with your code here
        new_message = ""
        self.shift = shift
        dict1 = self.build_shift_dict(shift)
        dict2=list(self.message_text)

        for char in dict2 :
                if char in string.ascii_lowercase:
                        new_message += dict1.get(char)
                elif char in string.digits:
                        new_message += char
                elif char in string.whitespace:
                        new_message += char
                elif char in string.punctuation:
                        new_message += char
        return new_message


