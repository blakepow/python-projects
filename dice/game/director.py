from game.thrower import Thrower

class Director:
    def __init__(self):
        self.keep_playing = True
        self.score = 0
        self.thrower = Thrower()

    def start_game(self):
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        self.thrower.throw_dice()
        
    def do_updates(self):
        points = self.thrower.get_points()
        self.score += points
        
    def do_outputs(self):
        print(f"\nYou rolled: {self.thrower.dice}")
        print(f"Your score is: {self.score}")
        if self.thrower.can_throw():
            choice = input("Roll again? [y/n] ")
            self.keep_playing = (choice == "y")
        else:
            self.keep_playing = False