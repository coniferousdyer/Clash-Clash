import os
from colorama import Fore
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
            "width": os.get_terminal_size().columns - 1,
            "height": os.get_terminal_size().lines - 1,
        }

        # Create the town hall
        town_hall = TownHall(
            location={
                "x": self.size["width"] // 2,
                "y": self.size["height"] // 2,
            },
        )

        # - buildings = town hall + huts + cannons.
        # - generate_huts and generate_cannons will append to the buildings array
        # so that position availability can be checked.
        # - generate_walls will append to the walls array and generates them around
        # the town hall.
        self.buildings = [town_hall]
        self.generate_walls()
        self.generate_huts()
        self.generate_cannons()

        # Predefined spawn locations for troops
        self.spawning_points = [
            {"x": 0, "y": 0},
            {"x": 0, "y": self.size["height"] - 1},
            {"x": self.size["width"] - 1, "y": 0},
        ]

    def generate_walls(self):
        """
        Generate walls around the town hall.
        """

        town_hall_location = self.buildings[0].location

        # Generating top and bottom walls
        for i in range(
            town_hall_location["x"] - 2,
            town_hall_location["x"] + self.buildings[0].size["width"] + 1,
        ):
            self.buildings.append(Wall({"x": i, "y": town_hall_location["y"] - 1}))
            self.buildings.append(
                Wall(
                    {
                        "x": i,
                        "y": town_hall_location["y"]
                        + self.buildings[0].size["height"]
                        + 1,
                    }
                )
            )

        # Generating left and right walls
        for i in range(
            town_hall_location["y"] - 1,
            town_hall_location["y"] + self.buildings[0].size["height"] + 2,
        ):
            self.buildings.append(Wall({"x": town_hall_location["x"] - 2, "y": i}))
            self.buildings.append(
                Wall(
                    {
                        "x": town_hall_location["x"]
                        + self.buildings[0].size["width"]
                        + 1,
                        "y": i,
                    }
                )
            )

    def generate_huts(self):
        """
        Generate huts.
        """

        # Generate huts at coordinates (10, 10), (30, 30), (190, 15), (100, 45) and (190, 80)
        self.buildings.append(Hut({"x": 10, "y": 10}))
        self.buildings.append(Hut({"x": 30, "y": 30}))
        self.buildings.append(Hut({"x": 190, "y": 15}))
        self.buildings.append(Hut({"x": 100, "y": 45}))
        self.buildings.append(Hut({"x": 190, "y": 25}))

    def generate_cannons(self):
        """
        Generate cannons.
        """

        # Generate cannons at coordinates (20, 20), (150, 10) and (140, 25)
        self.buildings.append(Cannon({"x": 20, "y": 20}))
        self.buildings.append(Cannon({"x": 150, "y": 10}))
        self.buildings.append(Cannon({"x": 140, "y": 25}))

    def draw(self, grid):
        """
        Draw the village.
        """

        # Fill the grid with the buildings
        for building in self.buildings:
            building.draw(grid)