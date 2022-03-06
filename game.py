from time import sleep
import os
from components.village import Village


class Game():
    """
    The Game class sets up the game.
    """

    def __init__(self):
        """
        Initialize the Game class.
        """

        # Create the village
        self.village = Village()

        # Start the game loop, running the game
        self.start_game_loop()

    def start_game_loop(self):
        """
        Starts the game loop.
        """

        # Run the game loop
        while True:
            os.system("clear")

            # Draw the village
            self.village.draw()

            # Sleep for a bit
            sleep(0.2)