import os
import random
from time import sleep
from .building import TownHall, Hut, Wall, Cannon


class Village:
    """
    The Village class handles the village details.
    """

    def __init__(self):
        """
        Initialize the Village class.
        """

        # Set the number of buildings
        num_huts, num_cannons = random.randint(5, 11), random.randint(2, 11)

        # Generate the buildings
        self.town_hall = TownHall(
            location={
                "x": os.get_terminal_size().lines // 2,
                "y": os.get_terminal_size().columns // 2,
            },
        )

        # Store the buildings
        self.buildings = [self.town_hall]

        # Create the huts and cannons
        self.huts = self.generate_huts(num_huts)
        self.cannons = self.generate_cannons(num_cannons)

        # Store the buildings
        self.buildings.extend(self.huts + self.cannons)

        # Predefined spawn locations for troops
        self.spawning_points = [
            {"x": 0, "y": 0},
            {"x": 0, "y": os.get_terminal_size().columns},
            {"x": os.get_terminal_size().lines, "y": 0},
        ]

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
            if (L["x"] >= bR["x"] or bL["x"] >= R["x"]) and (
                R["y"] >= bL["y"] or bR["y"] >= L["y"]
            ):
                return False

        # If the buildings are not overlapping, return True
        return True

    def generate_huts(self, num_huts):
        """
        Generate the huts.
        """

        huts = []

        for i in range(num_huts):
            # Generate a random position
            position = {
                "x": random.randint(0, os.get_terminal_size().lines - 3),
                "y": random.randint(0, os.get_terminal_size().columns - 3),
            }

            # Check if the position is available
            while not self.check_position_availability(
                position=position, size={"width": 2, "height": 2}
            ):
                position["x"] = random.randint(0, os.get_terminal_size().lines - 3)
                position["y"] = random.randint(0, os.get_terminal_size().columns - 3)

            # Add the hut to the array
            huts.append(Hut(position))

        return huts

    def generate_cannons(self, num_cannons):
        """
        Generate the cannons.
        """

        cannons = []

        for i in range(num_cannons):
            # Generate a random position
            position = {
                "x": random.randint(0, os.get_terminal_size().lines - 2),
                "y": random.randint(0, os.get_terminal_size().columns - 2),
            }

            # Check if the position is available
            while not self.check_position_availability(
                position=position, size={"width": 1, "height": 1}
            ):
                position["x"] = random.randint(0, os.get_terminal_size().lines - 2)
                position["y"] = random.randint(0, os.get_terminal_size().columns - 2)

            # Add the cannon to the array
            cannons.append(Cannon(position))

        return cannons

    def draw(self):
        """
        Draw the village.
        """

        pass
