import random
from game import constants
from game.action import Action
from arcade import View

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        paddle = cast["paddle"][0]

        balls_to_remove = []

        for ball in cast["balls"]:
            self._handle_wall_bounce(ball)
            self._handle_paddle_bounce(ball, paddle)

            bricks = cast["bricks"]
            self._handle_brick_collision(ball, bricks)

            if constants.BALLS_CAN_DIE and self._is_off_screen(ball):
                balls_to_remove.append(ball)

        for ball in balls_to_remove:
            cast["balls"].remove(ball)

        if not cast["balls"]:
            pass
            #end_view = EndView(False)
            #window.show_view(end_view)
            
        
        if not cast["bricks"]:
            pass
            #end_view = EndView(True)
            #window.show_view(start_view)

    def _handle_wall_bounce(self, ball):
        ball_x = ball.center_x
        ball_y = ball.center_y

        # Check for bounce on walls
        if ball_x <= 0 or ball_x >= constants.MAX_X:
            ball.bounce_vertical()

        if ball_y >= constants.MAX_Y:
            ball.bounce_horizontal()
        
        if not constants.BALLS_CAN_DIE and ball_y <= 0:
            ball.bounce_horizontal()
    
    def _handle_paddle_bounce(self, ball, paddle):
        # This makes use of the `Sprite` functionality
        if paddle.collides_with_sprite(ball):
            # Ball and paddle collide!
            ball.bounce_horizontal()

    def _handle_brick_collision(self, ball, bricks):
        brick_to_remove = None

        for brick in bricks:
            # This makes use of the `Sprite` functionality
            if ball.collides_with_sprite(brick):
                ball.bounce_horizontal()
                brick_to_remove = brick
        
        if brick_to_remove != None:
            bricks.remove(brick_to_remove)

    def _is_off_screen(self, ball):
        return ball.center_y < 0