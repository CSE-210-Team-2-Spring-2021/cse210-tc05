import random


class Jumper():
    """ This class determines the how many lives are left to guess. It also determines the word which is to be guessed and the parachute


        Stereotype:
          Information Holder


        Attributes:
          lives (interger): The number of "lives" the Riddler has, the number starts at 5.
          words (list): This is a list of words that can be the secret word to be guessed.
          secret_word (string): The word that will be guessed by the Riddler.
          man (list): Creates the parachute and the Jumper to be printed to the screen.
  """

    def __init__(self):
        """ Class constructor. Declares and initializes instance attributes.

            Args:
              self (Jumper): an instance of Jumper.
        """
        self.lives = 5
        self.words = []
        self.secret_word = ""
        self.man = ['  ___  ', ' /___\ ', ' \   / ', '  \ /',
                    '   0   ', '  /|\  ', '  / \  ', '\n', '^^^^^^^']

    def choose_word(self, list):
        """ Selects words from words list to give a random word to guess.
            Args:
              self (Jumper): an instance of Jumper
        """
        self.secret_word = random.choice(list)

    def update_lives(self, score):
        """ Takes in an int parameter (-1 or 0) and will simply add the parameter to lives and will also remove first item in man if parameter == -1

            Args:
              self (Jumper): an instance of Jumper.
        """
        if score == -1:
            self.man.pop(0)
            self.lives -= 1
