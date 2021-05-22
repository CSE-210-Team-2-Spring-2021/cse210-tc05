import random
from tkinter import filedialog

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
        words_file = filedialog.askopenfile()
        secret_words_list = words_file.readlines()
        return secret_words_list

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

    def write(self, text, list):
        """Displays the given text on the screen. 

        Args: 
            self (Screen): An instance of Screen.
            text (string): The text to display.
            list (list):  The jumper man to display.
        """
        # print a string from 
        print(text)

        # print out a list that is passed as arg
        for thing in list:
            print(thing)

    def game_over (self, game_won, game_lost):
        """Checks for if game continues or is over and then prints end message

        Args: game continue(bool): game continues on to next guess 
              game endd(bool): game over message appears
        """
        if game_won == True and game_lost == False:
            print("Congratulations, you guessed the secret word and saved the jumper!")

        if game_lost == True and game_won == False:
            print("You ran out of lives, and so did the jumper. Better luck next time.")
