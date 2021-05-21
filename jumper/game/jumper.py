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
        self.man = ['  ___  ', ' /___\ ', ' \   / ', '\ /',
                    '   0   ', '  /|\  ', '  / \  ', '\n', '^^^^^^^']

    def choose_word(self):
        """ Selects words from words list to give a random word to guess.
            Args:
              self (Jumper): an instance of Jumper
        """
        random.shuffle(self.words)
        for word in self.words:
            self.secret_word = word
        return self.secret_word

    def update_lives(self):
        """ Takes in an int parameter (-1 or 0) and will simply add the parameter to lives and will also remove first item in man if parameter == -1

            Args:
              self (Jumper): an instance of Jumper.
        """
        if self.guess != self.secret_word:
            return -1
        elif self.guess == self.secret_word:
            return 0

    def print_jumper(self):
        """ This method prints the jumper and parachute to the screen.

            Args:
              self (Jumper): an instance of Jumper.
        """
        for i in self.man:
            print(*self.man, sep="\n")
