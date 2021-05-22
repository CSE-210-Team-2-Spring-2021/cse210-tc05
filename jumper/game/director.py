from game.jumper import Jumper
from game.riddler import Riddler
from game.console import Console

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller/Coordinator

    Attributes:
        console (Console): An instance of the class of objects known as Console.
        jumper (Jumper): An instance of the class of objects known as Jumper
        riddler (Rabbit): An instance of the class of objects known as Riddler.
        riddle (string): Stores the secret word between methods.
        guesss (string): Stores the user's guess between methods.
        game_won (boolean): Whether the game has been won or not.
        game_lost (boolean): Whether the game has been lost or not.
        keep_playing (boolean): Whether or not the game can continue.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.console = Console()
        self.jumper = Jumper()
        self.riddler = Riddler()
        self.riddle = ""
        self.guess = ""
        self.game_won = False
        self.game_lost = False
        self.keep_playing = True

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        
        file_temp = self.console.read_file()
        self.jumper.choose_word(file_temp)
        self.riddler.split_list(self.jumper.secret_word)
        self.riddler.create_hidden_letters_list(self.jumper.secret_word)
        
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means retrieving the user's guess.

        Args:
            self (Director): An instance of Director.
        """

        self.guess = self.console.get_guess()

    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means the riddler informs us if the guess was correct and
        the jumper updates the parachute accordingly.

        Args:
            self (Director): An instance of Director.
        """
        answer = self.riddler.compare_letter(self.guess, self.jumper.secret_word)
        self.jumper.update_lives(answer)


        if self.riddler.hidden_word_revealed():
            self.game_won = True
            self.console.game_over (self.game_won, self.game_lost)

        elif self.jumper.lives <= 0:
            self.game_lost = True
            self.console.game_over (self.game_won, self.game_lost)
            self.console.write(f"The secret word was: {self.jumper.secret_word}", [])

        if self.game_won or self.game_lost:
            self.keep_playing = False


    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that the letter is added or a line is cut.

        Args:
            self (Director): An instance of Director.
        """

        self.console.write(self.riddler.hidden_letters_list, self.jumper.man)