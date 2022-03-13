import signal
import subprocess
from src.utils.menu import print_menu
from src.utils.cursor import Cursor
from src.utils.input import Input
from src import Game


def main():
    """
    The main function.
    """

    # Ignore SIGINT
    signal.signal(signal.SIGINT, signal.SIG_IGN)

    # Initialize the input class
    input_ = Input()

    # Initialize the cursor class
    cursor = Cursor()

    # Play background music
    proc = subprocess.Popen(["mpg123", "--loop", "10", "./src/assets/music.mp3"])

    # Print the menu
    print_menu(proc, input_)

    # Start the game
    game = Game(proc, input_)

if __name__ == '__main__':
    main()