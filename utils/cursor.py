import atexit


class Cursor:
    """
    The Cursor class handles cursor display.
    """

    def __init__(self):
        """
        Initialize the Cursor class, hiding the cursor.
        """

        # Hide the cursor
        print("\033[?25l", end="")

        # Show the cursor when exiting
        atexit.register(self.exit_handler)
    
    def exit_handler(self):
        """
        Restore the cursor when exiting.
        """

        # Show the cursor
        print("\033[?25h", end="")