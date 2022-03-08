from time import sleep
import os
from colorama import Fore
from components.village import Village
from components.king import King


class Game():
    """
    The Game class sets up the game.
    """

    def __init__(self, input_):
        """
        Initialize the Game class.
        """

        self.FRAME_RATE = 0.1

        # Create the grid (a 2D array making the job of representing the game state easier)
        self.grid = [
            [{"symbol": " ", "color": None}] * (os.get_terminal_size().columns - 1)
            for _ in range(os.get_terminal_size().lines - 1)
        ]

        # Create the village
        self.village = Village()
        self.king = King()

        # Start the game loop, running the game
        self.start_game_loop(input_)

    def clear_grid(self):
        """
        Clear the grid.
        """

        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                self.grid[i][j] = {"symbol": " ", "color": None}

    def print_grid(self):
        """
        Print the grid.
        """

        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j]["symbol"] != " ":
                    print(self.grid[i][j]["color"], end="")
                    print(self.grid[i][j]["symbol"], end="")
                    print(Fore.RESET, end="")
                else:
                    print(self.grid[i][j]["symbol"], end="")
            print()


    def start_game_loop(self, input_):
        """
        Starts the game loop.
        """

        # Run the game loop
        while True:
            # Clear screen and grid
            os.system("clear")
            self.clear_grid()

            # Draw the village and king in the grid
            self.village.draw(self.grid)
            self.king.draw(self.grid)
            
            # Print the grid
            self.print_grid()

            # Check for input
            if input_.if_key_pressed():
                # Get the input
                key = input_.get_input().lower()

                # Quit the game
                if key == "q":
                    os.system("clear")
                    exit()
                
                # Move king down
                if key == "s":
                    self.king.move_down(self.grid)

                # Move king up
                if key == "w":
                    self.king.move_up(self.grid)

                # Move king left
                if key == "a":
                    self.king.move_left(self.grid)

                # Move king right
                if key == "d":
                    self.king.move_right(self.grid)
                
            # Sleep for a bit
            sleep(self.FRAME_RATE)