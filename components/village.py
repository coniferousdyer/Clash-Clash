import os
import random
from .building import TownHall, Hut, Wall, Cannon


class Village:
    """
    The Village class handles the village details.
    """

    def __init__(self):
        """
        Initialize the Village class.
        """

        # Set the dimensions of the village
        self.size = {
            "width": os.get_terminal_size().columns,
            "height": os.get_terminal_size().lines,
        }

        # Set the number of buildings
        num_huts, num_cannons = random.randint(5, 11), random.randint(2, 11)

        # Create the town hall
        town_hall = TownHall(
            location={
                "x": self.size["width"] // 2,
                "y": self.size["height"] // 2,
            },
        )

        # buildings = town hall + huts + cannons.
        # generate_huts and generate_cannons will append to the buildings array
        # so that position availability can be checked.
        self.buildings = [town_hall]
        self.generate_huts(num_huts)
        self.generate_cannons(num_cannons)

        # Predefined spawn locations for troops
        self.spawning_points = [
            {"x": 0, "y": 0},
            {"x": 0, "y": self.size["height"] - 1},
            {"x": self.size["width"] - 1, "y": 0},
        ]

        # Create the grid (a 2D array making the job of representing the village easier)
        self.grid = []
        for i in range(self.size["height"]):
            self.grid.append([])
            for j in range(self.size["width"]):
                self.grid[i].append(" ")

        # Fill the grid with the buildings
        for building in self.buildings:
            for i in range(building.size["height"]):
                for j in range(building.size["width"]):
                    self.grid[building.location["y"] + i][
                        building.location["x"] + j
                    ] = building.symbol

    def check_position_availability(self, position, size):
        """
        Check if a position (x, y) for a building of given size is available.
        """

        # Storing the end points (at the diagonal) of the building
        L = position
        R = {
            "x": position["x"] + size["width"],
            "y": position["y"] + size["height"],
        }

        # Check if the 2 buildings are not overlapping
        for building in self.buildings:
            # Storing end points of the building
            bL = building.location
            bR = {
                "x": building.location["x"] + building.size["width"],
                "y": building.location["y"] + building.size["height"],
            }

            # Check if the buildings are overlapping
            if not (L["x"] >= bR["x"] or bL["x"] >= R["x"]) and not (
                R["y"] >= bL["y"] or bR["y"] >= L["y"]
            ):
                return False

        # If the buildings are not overlapping, return True
        return True

    def generate_huts(self, num_huts):
        """
        Generate the huts.
        """

        for i in range(num_huts):
            # Generate a random position
            position = {
                "x": random.randint(1, os.get_terminal_size().columns - 5),
                "y": random.randint(1, os.get_terminal_size().lines - 5),
            }

            # Check if the position is available
            while not self.check_position_availability(
                position=position, size={"width": 2, "height": 2}
            ):
                position["x"] = random.randint(1, os.get_terminal_size().columns - 5)
                position["y"] = random.randint(1, os.get_terminal_size().lines - 5)

            # Add the hut to the array
            self.buildings.append(Hut(position))

    def generate_cannons(self, num_cannons):
        """
        Generate the cannons.
        """

        for i in range(num_cannons):
            # Generate a random position
            position = {
                "x": random.randint(1, os.get_terminal_size().columns - 5),
                "y": random.randint(1, os.get_terminal_size().lines - 5),
            }

            # Check if the position is available
            while not self.check_position_availability(
                position=position, size={"width": 1, "height": 1}
            ):
                position["x"] = random.randint(1, os.get_terminal_size().columns - 5)
                position["y"] = random.randint(1, os.get_terminal_size().lines - 5)

            # Add the cannon to the array
            self.buildings.append(Cannon(position))

    def draw(self):
        """
        Draw the village.
        """

        # We iterate through each square of the village, checking if it is
        # occupied by a building. If it is, we add the particular symbol. However,
        # if it is not occupied, we add a space. This logic is implemented via the
        # grid array, as printing the buildings directly to the terminal might be
        # difficult, with the issue of newlines and such.
        for i in range(self.size["height"]):
            for j in range(self.size["width"]):
                print(self.grid[i][j], end="")
            print()
