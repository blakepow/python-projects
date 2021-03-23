from game.card import Card

import random

class Dealer:
    def __init__(self):
        self.card = Card()
        self.playing = True

    def start_game(self):
        self.play()

    def play(self):
        while self.playing == True:
            if self.card.score > 0:
                self.play_more = input("Would you like to play more? [y/n]: ")
                if self.play_more == "y":
                    print(f"The current card is {self.card.card1}")
                    self.card.draw_card()
                elif self.play_more == "n":
                    print(f'Your final score is {self.card.score}')
                    self.playing = False
            else: 
                print("You lost")
                self.playing = False
