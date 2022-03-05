from signal import signal
import signal
from menu import print_menu
from utils.cursor import Cursor
from utils.input import Input
from game import Game


def main():
    """
    The main function.
    """

    # Ignore SIGINT
    # signal.signal(signal.SIGINT, signal.SIG_IGN)

    # Initialize the input class
    input_ = Input()

    # Initialize the cursor class
    cursor = Cursor()

    # Print the menu
    print_menu(input_)

    # Start the game
    game = Game()

if __name__ == '__main__':
    main()