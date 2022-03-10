class Rage:
    """
    The Rage spell.
    """

    def __init__(self):
        """
        Initialize the Rage spell.
        """

        self.is_activated = True

    def action(self, troops):
        """
        Double movement speed and damage for all troops for the specified duration.
        """

        for troop in troops:
            if troop.is_dead:
                continue

            troop.damage *= 2
            troop.speed *= 2


class Heal:
    """
    The Heal spell.
    """

    def __init__(self):
        """
        Initialize the Heal spell.
        """

        self.is_activated = True

    def action(self, troops):
        """
        Increase current health by 150% for all troops.
        """

        for troop in troops:
            if troop.is_dead:
                continue

            if troop.health * 1.5 <= troop.max_health:
                troop.health *= 1.5
            else:
                troop.health = troop.max_health
