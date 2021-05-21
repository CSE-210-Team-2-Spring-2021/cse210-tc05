import random

class Console:
    """A code template for a computer console. The responsibility of this 
    class of objects is to get text or numerical input and display text output.
    
    Stereotype:
        Service Provider, Interfacer

    Attributes:
        prompt (string): The prompt to display on each line.
    """
     
    def read_file(self):
        """Read external text file for list of words to choose from to pass to Jumper class.

        Args: 
            words (list): open text file and store as variable to pass.

        Returns:
            list: The list of words file to pick from.
        """

        # open the text file with list of words
        with open("secret_words_list.txt") as secret_words_file:
        
            return secret_words_file

    def get_guess(self):
        """Gets letter input from the user through the screen.

        Args: 
            self (Screen): An instance of Screen.
            
        Returns:
            string: Letter guess from user
        """
        
        # prompt user for single letter guess
        guess = input("Guess a letter [a-z]: ")
    
        return guess
