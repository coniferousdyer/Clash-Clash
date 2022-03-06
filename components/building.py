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
        self.color = Fore.GREEN


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

        # Set the building's symbol
        self.symbol = "T"


class Hut(Building):
    """
    The Hut class handles the hut details.
    """

    def __init__(self, location, size={"width": 2, "height": 2}, health=50):
        """
        Initialize the Hut class.
        """

        # Call the parent class' constructor
        super().__init__(location, size, health)

        # Set the building's symbol
        self.symbol = "H"


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

        # Set the building's symbol
        self.symbol = "W"


class Cannon(Building):
    """
    The Cannon class handles the cannon details.
    """

    def __init__(self, location, size={"width": 2, "height": 2}, health=40):
        """
        Initialize the Cannon class.
        """

        # Call the parent class' constructor
        super().__init__(location, size, health)

        # Set the building's symbol
        self.symbol = "C"

        # Cannon-specific details
        self.damage = 10
        self.range = 10
        self.target = None
