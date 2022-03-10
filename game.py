from time import sleep
import os
from colorama import Fore
from components.village import Village
from components.building import Cannon
from components.troop import King, Barbarian
from components.spell import Heal, Rage


class Game:
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
        self.king = King(location=self.village.spawning_points[0])
        self.barbarians = []
        self.spells = []

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

    def draw_king_healthbar(self):
        """
        Draw the king's healthbar into the grid
        """

        j = 0
        for char in "Health:":
            self.grid[0][j] = {"symbol": char, "color": Fore.WHITE}
            j += 1

        for i in range(len("Health:"), self.king.health + len("Health:")):
            self.grid[0][i] = {"symbol": "█", "color": self.king.hit_color}

    def start_game_loop(self, input_):
        """
        Starts the game loop.
        """

        # Run the game loop
        while True:
            # -----------UPDATE GAME STATE-----------#

            # Clear screen and grid
            os.system("clear")
            self.clear_grid()

            # Draw the king's healthbar
            self.draw_king_healthbar()

            # Activate any cast spells
            for spell in self.spells:
                if spell.is_activated:
                    spell.action([self.king] + self.barbarians)
                    spell.is_activated = False

            # Draw the village and king in the grid
            self.village.draw(self.grid)
            self.king.draw(self.grid)

            # For each cannon, set targets if they are not set, and shoot
            for building in self.village.buildings:
                if isinstance(building, Cannon):
                    if building.target is None:
                        building.find_target([self.king] + self.barbarians)
                    building.shoot()

            # Draw barbarians, set targets if they are not set, move them and attack
            for barbarian in self.barbarians:
                barbarian.draw(self.grid)
                if barbarian.target is None:
                    barbarian.find_target(self.village.buildings)
                barbarian.move(self.grid, self.village.buildings)
                barbarian.attack()

            # Print the grid
            self.print_grid()

            # -----------TAKE USER INPUT-----------#

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
                    self.king.move_down(self.grid, self.village.buildings)

                # Move king up
                if key == "w":
                    self.king.move_up(self.grid, self.village.buildings)

                # Move king left
                if key == "a":
                    self.king.move_left(self.grid, self.village.buildings)

                # Move king right
                if key == "d":
                    self.king.move_right(self.grid, self.village.buildings)

                # Make king attack
                if key == " ":
                    self.king.attack(self.grid, self.village.buildings)

                # Spawn a barbarian at a spawning point
                if key in ["1", "2", "3"]:
                    self.barbarians.append(
                        Barbarian(
                            location=self.village.spawning_points[int(key) - 1],
                        )
                    )

                # Activate Rage spell
                if key == "r":
                    already_active = False

                    # Check if the spell is already active
                    for spell in self.spells:
                        if isinstance(spell, Rage):
                            already_active = True
                            break

                    # If the spell is not active, activate it
                    if not already_active:
                        self.spells.append(Rage())

                # Activate Heal spell
                if key == "h":
                    already_active = False

                    # Check if the spell is already active
                    for spell in self.spells:
                        if isinstance(spell, Heal):
                            already_active = True
                            break

                    # If the spell is not active, activate it
                    if not already_active:
                        self.spells.append(Heal())

            # Sleep for a bit
            sleep(self.FRAME_RATE)
