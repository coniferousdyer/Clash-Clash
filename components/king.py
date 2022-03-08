from colorama import Fore
import os


class King:
    """
    The King class handles the King character.
    """

    def __init__(self):
        """
        Initialize the King class.
        """

        self.location = {"x": 0, "y": 0}
        self.size = {"width": 3, "height": 4}
        self.health = 100
        self.damage = 5
        self.speed = 1

        # Set the King's ASCII art and color
        self.color = Fore.MAGENTA
        self.art = [
            " M ",
            " O ",
            "/|\\",
            "/ \\",
        ]

    def draw(self, grid):
        """
        Draw the king.
        """

        # Draw the king in the grid
        for i in range(self.size["height"]):
            for j in range(self.size["width"]):
                grid[self.location["y"] + i][self.location["x"] + j] = {
                    "symbol": self.art[i][j],
                    "color": self.color,
                }

    def move_down(self, grid):
        """
        Move the king down.
        """

        # Checking if position is not out of bounds
        if not (
            self.location["y"] + self.size["height"] + self.speed
            <= os.get_terminal_size().lines - 1
        ):
            return

        is_position_free = True

        # Checking if position is free
        for i in range(self.size["width"]):
            if (
                grid[self.location["y"] + self.size["height"]][self.location["x"] + i][
                    "symbol"
                ]
                != " "
            ):
                is_position_free = False

        if not is_position_free:
            return

        self.location["y"] += self.speed

    def move_up(self, grid):
        """
        Move the king up.
        """

        # Checking if position is not out of bounds
        if not self.location["y"] - self.speed >= 0:
            return

        is_position_free = True

        # Checking if position is free
        for i in range(self.size["width"]):
            if (
                grid[self.location["y"] - self.speed][self.location["x"] + i]["symbol"]
                != " "
            ):
                is_position_free = False

        if not is_position_free:
            return

        self.location["y"] -= self.speed

    def move_left(self, grid):
        """
        Move the king left.
        """

        # Checking if position is not out of bounds
        if not self.location["x"] - self.speed >= 0:
            return

        is_position_free = True

        # Checking if position is free
        for i in range(self.size["height"]):
            if (
                grid[self.location["y"] + i][self.location["x"] - self.speed]["symbol"]
                != " "
            ):
                is_position_free = False

        if not is_position_free:
            return

        self.location["x"] -= self.speed

    def move_right(self, grid):
        """
        Move the king right.
        """

        # Checking if position is not out of bounds
        if not (
            self.location["x"] + self.size["width"] + self.speed
            <= os.get_terminal_size().columns - 1
        ):
            return

        is_position_free = True

        # Checking if position is free
        for i in range(self.size["height"]):
            if (
                grid[self.location["y"] + i][self.location["x"] + self.size["width"]][
                    "symbol"
                ]
                != " "
            ):
                is_position_free = False

        if not is_position_free:
            return

        self.location["x"] += self.speed
