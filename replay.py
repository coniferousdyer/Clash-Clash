import os
import json
import subprocess
from src.utils.cursor import Cursor
from src import Game


def main():
    """
    The main replay function.
    """

    # Play background music
    proc = subprocess.Popen(["mpg123", "--loop", "10", "./src/assets/music.mp3"])

    # Initialize the cursor class
    cursor = Cursor()

    os.system("clear")
    print("Replays:\n")

    # Load the replays
    replays = os.listdir("./replays")
    for i in range(len(replays)):
        print(f"{i}. {replays[i]}")

    index = input("\nEnter corresponding number to activate replay (and Q to quit): ")

    if index == "q" or index == "Q":
        os.system("clear")
        proc.terminate()
        exit()
    else:
        with open(f"./replays/{replays[int(index)]}", "r") as replay_file:
            keys = json.load(replay_file)
        game = Game(proc, input_=None, replay=True, keys=keys)


if __name__ == "__main__":
    main()
