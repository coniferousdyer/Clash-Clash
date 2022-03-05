from time import sleep
from colorama import Fore
from utils.art import get_homescreen_art
import os


def print_menu(input_):
    """
    Prints the opening game menu.
    """

    homescreen_art = get_homescreen_art()
    color_loop = [Fore.RED, Fore.MAGENTA, Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.YELLOW]

    # An iterator for the color loop
    i = 0

    # Print the art, looping through the colors
    while True:
        # Clear the screen
        os.system("clear")

        # Print the art
        print("\n" * (os.get_terminal_size().lines // 4))
        print(color_loop[i])
        for art_line in homescreen_art:
            print(art_line.center(os.get_terminal_size().columns))

        # Reset the color
        print(Fore.RESET)

        # Print instructions to start
        print("\n"*3)
        print("Press S to start, Q to exit and R to view replays.".center(os.get_terminal_size().columns))

        # Increment the color loop iterator
        i = (i + 1) % len(color_loop)

        # Check for input
        if input_.if_key_pressed():
            # Get the input
            key = input_.get_input().lower()

            # Check for the quit key
            if key == "q":
                os.system("clear")
                exit()
            
            # Check for the start key
            if key == "s":
                os.system("clear")
                return             
            
        # Wait for a while to reduce frame rate
        sleep(0.1)
