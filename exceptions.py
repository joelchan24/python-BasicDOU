class DOU_Error:
    
    def __init__ (self,message):
        super().__init__(message)
    

   


class example():

    def __init__(self,word):
        self.word = word


    def getWord(self):
        if self.word.isalpha():
            print("Well done, valid word")
        else:
            raise DOU_Error("string has any character which is not a word character.") 


action=example("joel121")
action.getWord()