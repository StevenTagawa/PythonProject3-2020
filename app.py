"""This is the main module for the Phrase Hunter game."""

import game

# EXECUTION STARTS HERE
if __name__ == "__main__":
    try:
        while True:
            new_game = game.Game()
            # The start method returns True if the player wants to play again.
            if not new_game.start():
                break
    except KeyboardInterrupt:
        print("\nScript halted by user.")
# EXECUTION ENDS HERE
