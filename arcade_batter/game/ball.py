import random
from game import constants

import arcade

class Ball(arcade.Sprite):

    def __init__(self):
        super().__init__(constants.BALL_IMAGE)
        self.change_x = constants.BALL_SPEED * ((-1)^random.randint(1,2))
        self.change_y = constants.BALL_SPEED * ((-1)^random.randint(1,2))
        start_x = random.randint(0, constants.MAX_X - 10) + 5
        self.center_x = int(start_x)
        start_y = random.randint(0, 20) + constants.BALL_Y
        self.center_y = int(start_y)

    def bounce_horizontal(self):
        self.change_y = -1 * (self.change_y)

    def bounce_vertical(self):
        self.change_x = -1 * (self.change_x)