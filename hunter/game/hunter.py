import random

class Hunter:
    """A code template for a happless but lovable hunter with rhotacism. The 
    responsibility of this class of objects is to move from location to 
    location in pursuit of the Rabbit.
    
    Stereotype:
        Information Holder

    Attributes:
        location (integer): The location of the Hunter (1-1000).
        distance (list): The distance travelled with each move.
    """

    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args:
            self (Hunter): An instance of Hunter.
        """
        self.location = random.randint(1, 1000)
        self.distance = [0, 0] # start with two so get_message always works
    
    def get_message(self):
        """Gets a message from the hunter.

        Args:
            self (Hunter): An instance of Hunter.
        
        Returns:
            string: A message from the hunter.
        """
        message = "\nI'm hunting wabbits!"
        if self.distance[-1] == 0:
            message = "\nWhy, you wascally wabbit!"
        elif self.distance[-1] > self.distance[-2]:
            message = "\nShhh. Be vewy vewy quiet."
        elif self.distance[-1] < self.distance[-2]:
            message = "\nSay your pwayers, wabbit!"
        return message

    def move(self, location):
        """Moves to the given location and keeps track of the distance.

        Args:
            self (Hunter): An instance of Hunter.
        """
        distance = abs(self.location - location)
        self.distance.append(distance)
        self.location = location