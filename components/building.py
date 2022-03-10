from colorama import Fore


class Building:
    """
    The base Building class. All other types of buildings inherit from this class.
    """

    def __init__(self, location, size, health):
        """
        Initialize the Building class.
        """

        # Essential building details
        self.location = location
        self.size = size
        self.health = health
        self.max_health = health
        self.is_destroyed = False
        self.was_hit = False
        self.hit_color = Fore.GREEN

    def draw(self, grid):
        """
        Draw the building.
        """

        # Check if the building is destroyed
        if self.is_destroyed:
            return

        # Find the correct display color according to whether the building was hit
        color = self.color
        if self.was_hit:
            color = self.hit_color

        # Draw the building in the grid
        for i in range(self.size["height"]):
            for j in range(self.size["width"]):
                grid[self.location["y"] + i][self.location["x"] + j] = {
                    "symbol": self.art[i][j],
                    "color": color,
                }

        if self.was_hit:
            self.was_hit = False

    def take_damage(self, damage):
        """
        Take damage to the building.
        """

        self.health -= damage
        self.was_hit = True

        # Check if the building is destroyed
        if self.health <= 0:
            self.is_destroyed = True
            return

        # If less than 50% health left
        if self.health <= self.max_health / 2:
            self.hit_color = Fore.YELLOW

        # If less than 20% health left
        if self.health <= self.max_health / 5:
            self.hit_color = Fore.RED


class TownHall(Building):
    """
    The TownHall class handles the town hall details.
    """

    def __init__(self, location, size={"width": 3, "height": 4}, health=100):
        """
        Initialize the TownHall class.
        """

        # Call the parent class' constructor
        super().__init__(location, size, health)

        # Set the building's ASCII art and color
        self.color = Fore.WHITE
        self.art = [
            "/█\\",
            "|-|",
            "|█|",
            "|█|",
        ]


class Hut(Building):
    """
    The Hut class handles the hut details.
    """

    def __init__(self, location, size={"width": 3, "height": 2}, health=50):
        """
        Initialize the Hut class.
        """

        # Call the parent class' constructor
        super().__init__(location, size, health)

        # Set the building's ASCII art and color
        self.color = Fore.WHITE
        self.art = [
            "/-\\",
            "|█|",
        ]


class Wall(Building):
    """
    The Wall class handles the wall details.
    """

    def __init__(self, location, size={"width": 1, "height": 1}, health=10):
        """
        Initialize the Wall class.
        """

        # Call the parent class' constructor
        super().__init__(location, size, health)

        # Set the building's ASCII art and color
        self.color = Fore.WHITE
        self.art = ["*"]


class Cannon(Building):
    """
    The Cannon class handles the cannon details.
    """

    def __init__(self, location, size={"width": 3, "height": 3}, health=40):
        """
        Initialize the Cannon class.
        """

        # Call the parent class' constructor
        super().__init__(location, size, health)

        # Set the building's ASCII art and color
        self.color = Fore.WHITE
        self.art = [
            "███",
            "|o|",
            "/█\\",
        ]

        # Cannon-specific details
        self.damage = 10
        self.range = 15
        self.target = None
        self.ATTACK_INTERVAL = 10
        self.attack_time_left = self.ATTACK_INTERVAL

    def find_target(self, troops):
        """
        Find the closest troop in range.
        """

        for troop in troops:
            if troop.is_dead:
                continue

            min_distance = None
            min_distance_troop = None

            # Find the closest troop in range
            distance = abs(self.location["x"] - troop.location["x"]) + abs(
                self.location["y"] - troop.location["y"]
            )
            if distance <= self.range:
                if min_distance is None or distance < min_distance:
                    min_distance = distance
                    min_distance_troop = troop

            self.target = min_distance_troop

    def shoot(self):
        """
        Shoot the chosen target.
        """

        if self.target is None:
            return

        if self.attack_time_left <= 0:
            # Check if target is still in range
            distance_1 = abs(self.location["x"] - self.target.location["x"]) + abs(
                self.location["y"] - self.target.location["y"]
            )
            distance_2 = abs(
                self.location["x"]
                - (self.target.location["x"] + self.target.size["width"])
                + abs(self.location["y"] - self.target.location["y"])
            )
            distance_3 = abs(
                self.location["x"]
                - self.target.location["x"]
                + abs(
                    self.location["y"]
                    - (self.target.location["y"] + self.target.size["height"])
                )
            )
            distance_4 = abs(
                self.location["x"]
                - (self.target.location["x"] + self.target.size["width"])
                + abs(
                    self.location["y"]
                    - (self.target.location["y"] + self.target.size["height"])
                )
            )

            if (
                distance_1 <= self.range
                or distance_2 <= self.range
                or distance_3 <= self.range
                or distance_4 <= self.range
            ):
                self.target.take_damage(self.damage)
                self.attack_time_left = self.ATTACK_INTERVAL
        else:
            self.attack_time_left -= 1

    def draw(self, grid):
        """
        Draw the building.
        """

        # Check if the building is destroyed
        if self.is_destroyed:
            return

            if distance_1 <= self.range or distance_2 <= self.range:
                self.target.take_damage(self.damage)
                if self.target.is_dead:
                    self.target = None

            self.attack_time_left = self.ATTACK_INTERVAL
        else:
            self.attack_time_left -= 1
