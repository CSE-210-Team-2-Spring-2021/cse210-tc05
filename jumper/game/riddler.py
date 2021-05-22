class Riddler:
    """

    The class Riddler manage all the method regarding to show the secret word format, reveal guessed letters, keep or take lives away

    Stereotype:  Information Holder

    """
    #Class constructor. Declares and initializes instance attributes.
    def __init__(self):
        
        self.split_secret_word_list = []             #It will be filled with the split_secret_word_list method
        self.hidden_letters_list = []                   #It will be filled with the create_hidden_letters_list method


    #It will save a list with each letter from the secret word
    def split_list(self,secret_word):
            self.split_secret_word_list = list(secret_word)

    
    # Create lines (underscores) to indicate that a letter will be in that position, and also, there are as many lines as letters in the secret word.
    def create_hidden_letters_list(self, secret_word):
        for i in range(0,len(secret_word) - 1):
            self.hidden_letters_list.append("_")


    # Compare the prompt letter with the secret word.
    # If the letter is in the list. It will replace from the "Hidden word" list (hidden_letters_list) the corresponding underscore with the letter/s
    # It will return 0 if the letter is on the secret word
    # It will return -1 if the letter is not on the secret word and the player will lost a live 
    def compare_letter(self,guess,secret_word):
        letter_discovered = False
        for i in range(0,len(secret_word) - 1):
            if self.hidden_letters_list[i] == '_':
                if guess.lower() == self.split_secret_word_list[i]:
                    self.hidden_letters_list[i] = self.split_secret_word_list[i]
                    letter_discovered = True
        if letter_discovered:
            return(0)            
        
        if True:
            return (-1)


    # Check if all the underscores in split_secret_word_list were replaced with letters
    # Returns a Boolean value
    # If the user complete the list, it means that he wins and returns "True"
    # If the user has some underscores yet, means that some letters didn't be guessed yet, so the method will return "False"
    def hidden_word_revealed(self):
        underscores = self.hidden_letters_list.count("_")
        if underscores == 0:
            return True
        else:
            return False



