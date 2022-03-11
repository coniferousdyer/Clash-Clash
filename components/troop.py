from colorama import Fore
import copy
import os


class Troop:
    """
    The base Troop class. All other types of troops inherit from this class.
    """

    def __init__(self, location, size, health, damage, speed):
        """
        Initialize the Troop class.
        """

        # We use a copy of the location to prevent the original location from being modified.
        # We only do this here because a spawning point is provided as a location to the troop.
        self.location = copy.copy(location)
        self.previous_location = copy.copy(location)
        self.size = size
        self.health = health
        self.max_health = health
        self.damage = damage
        self.speed = speed
        self.direction = "right"
        self.was_hit = False
        self.hit_color = Fore.GREEN
        self.is_dead = False

    def draw(self, grid):
        """
        Draw the troop.
        """

        # Find the correct display color according to whether the troop was hit
        color = self.color
        if self.was_hit:
            color = self.hit_color

        # Draw the troop in the grid
        for i in range(self.size["height"]):
            for j in range(self.size["width"]):
                grid[self.location["y"] + i][self.location["x"] + j] = {
                    "symbol": self.art[i][j],
                    "color": color,
                }

        if self.was_hit:
            self.was_hit = False

    def move_down(self, grid, buildings):
        """
        Move the troop down.
        """

        if self.is_dead:
            return

        self.direction = "down"

        # Checking if position is not out of bounds
        if not (
            self.location["y"] + self.size["height"] + self.speed
            <= os.get_terminal_size().lines - 1
        ):
            return

        # Checking if position is free
        for i in range(self.size["width"]):
            if (
                grid[self.location["y"] + self.size["height"] - 1 + self.speed][
                    self.location["x"] + i
                ]["symbol"]
                != " "
            ):
                # Check if the position is occupied by a building. If not, the troop can move there.
                for building in buildings:
                    if building.is_destroyed:
                        continue

                    if (
                        self.location["y"] + self.size["height"] + self.speed
                        >= building.location["y"]
                        and self.location["y"] + self.size["height"] + self.speed
                        <= building.location["y"] + building.size["height"]
                    ):
                        if (
                            self.location["x"] + i >= building.location["x"]
                            and self.location["x"] + i
                            <= building.location["x"] + building.size["width"]
                        ):
                            return

        self.location["y"] += self.speed

    def move_up(self, grid, buildings):
        """
        Move the troop up.
        """

        if self.is_dead:
            return

        self.direction = "up"

        # Checking if position is not out of bounds
        if not self.location["y"] - self.speed >= 0:
            return

        # Checking if position is free
        for i in range(self.size["width"]):
            if (
                grid[self.location["y"] - self.speed][self.location["x"] + i]["symbol"]
                != " "
            ):
                # Check if the position is occupied by a building. If not, the troop can move there.
                for building in buildings:
                    if building.is_destroyed:
                        continue

                    if (
                        self.location["y"] - self.speed >= building.location["y"]
                        and self.location["y"] - self.speed
                        <= building.location["y"] + building.size["height"]
                    ):
                        if (
                            self.location["x"] + i >= building.location["x"]
                            and self.location["x"] + i
                            <= building.location["x"] + building.size["width"]
                        ):
                            return

        self.location["y"] -= self.speed

    def move_left(self, grid, buildings):
        """
        Move the troop left.
        """

        if self.is_dead:
            return

        self.direction = "left"

        # Checking if position is not out of bounds
        if not self.location["x"] - self.speed >= 0:
            return

        # Checking if position is free
        for i in range(self.size["height"]):
            if (
                grid[self.location["y"] + i][self.location["x"] - self.speed]["symbol"]
                != " "
            ):
                # Check if the position is occupied by a building. If not, the troop can move there.
                for building in buildings:
                    if building.is_destroyed:
                        continue

                    if (
                        self.location["y"] + i >= building.location["y"]
                        and self.location["y"] + i
                        <= building.location["y"] + building.size["height"]
                    ):
                        if (
                            self.location["x"] - self.speed >= building.location["x"]
                            and self.location["x"] - self.speed
                            <= building.location["x"] + building.size["width"]
                        ):
                            return

        self.location["x"] -= self.speed

    def move_right(self, grid, buildings):
        """
        Move the troop right.
        """

        if self.is_dead:
            return

        self.direction = "right"

        # Checking if position is not out of bounds
        if not (
            self.location["x"] + self.size["width"] + self.speed
            <= os.get_terminal_size().columns - 1
        ):
            return

        # Checking if position is free
        for i in range(self.size["height"]):
            if (
                grid[self.location["y"] + i][
                    self.location["x"] + self.size["width"] - 1 + self.speed
                ]["symbol"]
                != " "
            ):
                # Check if the position is occupied by a building. If not, the troop can move there.
                for building in buildings:
                    if building.is_destroyed:
                        continue

                    if (
                        self.location["y"] + i >= building.location["y"]
                        and self.location["y"] + i
                        <= building.location["y"] + building.size["height"]
                    ):
                        if (
                            self.location["x"] + self.size["width"] + self.speed
                            >= building.location["x"]
                            and self.location["x"] + self.size["width"] + self.speed
                            <= building.location["x"] + building.size["width"]
                        ):
                            return

        self.location["x"] += self.speed

    def take_damage(self, damage):
        """
        Take damage from the cannon.
        """

        self.health -= damage
        self.was_hit = True

        # Check if the building is destroyed
        if self.health <= 0:
            self.is_dead = True
            return

        # If less than 50% health left
        if self.health <= self.max_health / 2:
            self.hit_color = Fore.YELLOW

        # If less than 20% health left
        if self.health <= self.max_health / 5:
            self.hit_color = Fore.RED


class King(Troop):
    """
    The King class.
    """

    def __init__(
        self, location, size={"width": 3, "height": 4}, health=100, damage=5, speed=1
    ):
        """
        Initialize the King class.
        """

        # Call the parent class' constructor
        super().__init__(location, size, health, damage, speed)

        # Set the King's ASCII art and color
        self.color = Fore.MAGENTA
        self.art = [
            " M ",
            " O ",
            "/|\\",
            "/ \\",
        ]

    def attack(self, grid, buildings):
        """
        Attack the building depending on the direction of the king.
        """

        attack_location = {
            "x": self.location["x"],
            "y": self.location["y"],
        }

        if self.direction == "right":
            attack_location["x"] += self.size["width"] - 1 + self.speed
        elif self.direction == "left":
            attack_location["x"] -= self.speed
        elif self.direction == "up":
            attack_location["y"] -= self.speed
        elif self.direction == "down":
            attack_location["y"] += self.size["height"] - 1 + self.speed

        # Checking if position is not out of bounds
        if not (
            attack_location["x"] >= 0
            and attack_location["x"] <= os.get_terminal_size().columns - 1
            and attack_location["y"] >= 0
            and attack_location["y"] <= os.get_terminal_size().lines - 1
        ):
            return

        # Checking if position is free
        if grid[attack_location["y"]][attack_location["x"]]["symbol"] == " ":
            return

        # Find the building in that location
        for building in buildings:
            if building.is_destroyed:
                continue

            if (
                attack_location["y"] >= building.location["y"]
                and attack_location["y"]
                <= building.location["y"] + building.size["height"]
            ):
                if (
                    attack_location["x"] >= building.location["x"]
                    and attack_location["x"]
                    <= building.location["x"] + building.size["width"]
                ):
                    building.take_damage(self.damage)


class Barbarian(Troop):
    """
    The Barbarian class.
    """

    def __init__(
        self, location, size={"width": 1, "height": 2}, health=50, damage=2, speed=1
    ):
        """
        Initialize the Barbarian class.
        """

        # Call the parent class' constructor
        super().__init__(location, size, health, damage, speed)

        # The location of the barbarian's current target. If None, no target is set.
        self.target = None

        # Set the Barbarian's ASCII art and color
        self.color = Fore.WHITE
        self.art = [
            "O",
            "U",
        ]

    def find_target(self, buildings):
        """
        Find the building to attack.
        """

        # Looping through the buildings, finding the one with the least Manhattan distance
        # to the barbarian's current location. Manhattan distance = |x1 - x2| + |y1 - y2|.
        min_distance = None
        min_distance_building = None

        for building in buildings:
            # Exclude the building if it is destroyed
            if building.is_destroyed:
                continue

            distance = abs(self.location["x"] - building.location["x"]) + abs(
                self.location["y"] - building.location["y"]
            )

            if min_distance is None or distance < min_distance:
                min_distance = distance
                min_distance_building = building

        # Setting the barbarian's target to the building with the least Manhattan distance
        self.target = min_distance_building

    def move(self, grid, buildings):
        """
        Uses the Troop class' move_* methods to move towards its target.
        """

        # If the target is not set, do nothing
        if self.target is None:
            return

        self.previous_location = copy.copy(self.location)

        # If the target is set, move towards it
        if self.target.location["y"] > self.location["y"]:
            self.move_down(grid, buildings)
        if self.target.location["y"] < self.location["y"]:
            self.move_up(grid, buildings)
        if self.target.location["x"] > self.location["x"]:
            self.move_right(grid, buildings)
        if self.target.location["x"] < self.location["x"]:
            self.move_left(grid, buildings)

    def attack(self, grid, buildings):
        """
        Attack the Barbarian's chosen target.
        """

        # If the target is not set, do nothing
        if self.target is None:
            return

        # If the target is set and is near the barbarian, attack it
        distance = abs(self.location["x"] - self.target.location["x"]) + abs(
            self.location["y"] - self.target.location["y"]
        )
        if distance <= self.speed:
            self.target.take_damage(self.damage)
            if self.target.is_destroyed:
                self.target = None
        # If the barbarian cannot move because it is blocked by a building, and is out
        # of range of its target, destroy the squares in between the barbarian and the
        # target.
        elif (
            self.previous_location["y"] == self.location["y"]
            and self.previous_location["x"] == self.location["x"]
        ):
            for direction in ["up", "down", "left", "right"]:
                attack_location = {
                    "x": self.location["x"],
                    "y": self.location["y"],
                }

                if direction == "right":
                    attack_location["x"] += self.size["width"]
                    for i in range(self.size["height"]):
                        if (
                            grid[attack_location["y"] + i][attack_location["x"]][
                                "symbol"
                            ]
                            != " "
                        ):
                            attack_location["y"] += i
                            break

                elif direction == "left":
                    attack_location["x"] -= self.speed
                    for i in range(self.size["height"]):
                        if (
                            grid[attack_location["y"] + i][attack_location["x"]][
                                "symbol"
                            ]
                            != " "
                        ):
                            attack_location["y"] += i
                            break

                elif direction == "up":
                    attack_location["y"] -= self.speed
                    for i in range(self.size["width"]):
                        if (
                            grid[attack_location["y"]][attack_location["x"] + i][
                                "symbol"
                            ]
                            != " "
                        ):
                            attack_location["x"] += i
                            break

                elif direction == "down":
                    attack_location["y"] += self.size["height"]
                    for i in range(self.size["width"]):
                        if (
                            grid[attack_location["y"]][attack_location["x"] + i][
                                "symbol"
                            ]
                            != " "
                        ):
                            attack_location["x"] += i
                            break

                for building in buildings:
                    if building.is_destroyed:
                        continue

                    if (
                        attack_location["y"] >= building.location["y"]
                        and attack_location["y"]
                        <= building.location["y"] + building.size["height"]
                    ):
                        if (
                            attack_location["x"] >= building.location["x"]
                            and attack_location["x"]
                            <= building.location["x"] + building.size["width"]
                        ):
                            building.take_damage(self.damage)
                            break
