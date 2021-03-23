import random

class Card:

    def __init__(self):

        self.card1 = random.randint(1, 13)
        self.card2 = random.randint(1, 13)
        self.score = 300
        self.guess = ''

    def draw_card(self):
        self.guess = input("Higher or lower? [h/l]")
        if self.guess == 'h' or self.guess == 'l':
            self.get_points()
        else:
            print('Please input h for higher or l for lower')
            self.draw_card()
        
    def get_points(self):    
        if self.card1 > self.card2 and self.guess == "l":
            #score goes up 100
            print("Correct")
            self.score += 100
        elif self.card1 < self.card2 and self.guess == "l":
            #score goes down 75
            print('Wrong')
            self.score -= 75
        elif self.card1 < self.card2 and self.guess == "h":
            #score goes up 100
            print('Correct!')
            self.score += 100
        elif self.card1 > self.card2 and self.guess == "h":
            #score goes down 75
            print("Wrong")
            self.score -= 75
        self.new_cards()
        
    def new_cards(self):
            print(f"Your score is {self.score}")
            self.card1 = self.card2
            self.card2 = random.randint(1, 13)
            