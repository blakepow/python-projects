from game.console import Console
from game.jumper import Jumper
from game.word import Word
import random

class Director:

    def __init__(self):
        self.console = Console()
        self.jumper = Jumper()
        self.keep_playing = True
        self.word = Word()
    
    def start_game(self):
        #Iniciates the game loop to control the game
        while self.keep_playing:
            self.get_input()
            self.updates()
            self.do_outputs()
        

    def get_input(self):
        #Gets the new guess at the beginning of each round
        word = self.word.word
        message = self.jumper.get_parachute(word)
        self.console.write(message)
        letter = self.console.read_letter("Enter a letter [a-z]: ")
        self.word.play(letter)
        

    def updates(self):
        #Updates the game inforamtion(The jumper watches the word)
        tries = self.word.tries
        self.jumper.display_jumper(tries)
        



    def do_outputs(self):
        #Outputs the game information for each round(Word & Jumper)
        if self.word.tries >= 4:
            self.keep_playing = False
        
