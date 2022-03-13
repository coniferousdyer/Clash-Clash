import atexit
import sys
import termios
import atexit
from select import select


class Input:
    """
    The Input class handles user input.
    """

    def __init__(self):
        """
        Initialize the Input class, applying the required terminal settings.
        """

        self.fd = sys.stdin.fileno()
        self.old_settings = termios.tcgetattr(self.fd)

        # Disable echo and enable raw mode
        self.new_settings = termios.tcgetattr(self.fd)
        self.new_settings[3] = self.new_settings[3] & ~termios.ECHO & ~termios.ICANON
        termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.new_settings)

        # Register signal handler to restore settings
        atexit.register(self.exit_handler)
    
    def exit_handler(self):
        """
        Restore the old settings when exiting.
        """
        termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.old_settings)

    def get_input(self):
        """
        Get the user's input.
        """
        return sys.stdin.read(1)

    def if_key_pressed(self):
        """
        Check if a key was pressed.
        """
        return select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])
        