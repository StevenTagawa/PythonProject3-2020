"""This module contains the Game class for the Phrase Hunter game."""
import os
import random

import phrase


class Game:
    """Class encapsulating the Phrase Hunter game.

    Attributes:
    missed -- Tracks the number of incorrect guesses by the player.
    phrases -- A list of phrases used in the game.
    active_phrase -- The phrase used by the current instance.
    guesses -- Tracks the letters guessed by the player.

    Public Methods:
    start() -- Manages the gameplay.
    get_random_phrase() -- Picks a phrase to use in the game.
    welcome() -- Prints a welcome messages at the start of each game.
    get_guess() -- Gets a letter from the player.
    game_over() -- Prints a summary message after the game ends.

    Private Methods:
    _valid_guess() -- Verifies the validity of the player's guess.
    _clear() -- Clears the screen.
    _goodbye() -- Prints a goodbye message.
    _plural() -- Provides the correct form of the word "guess."
    _play_again() -- Asks the player if they want to play again.
    _check_yes_no() -- Checks the player's response to a yes/no question.
    """

    def __init__(self):
        self.missed = 0
        self.phrases = [
            phrase.Phrase("blessed are the cheesemakers"),
            phrase.Phrase("this parrot is no more"),
            phrase.Phrase("try and favour the other leg"),
            phrase.Phrase("your mother was a hamster"),
            phrase.Phrase("my hovercraft is full of eels")
        ]
        self.active_phrase = None
        self.guesses = []

    def start(self):
        """Manages gameplay.

        Arguments:  None.

        Returns:
        True if the player wants to play again; otherwise False.
        """
        self.active_phrase = self.get_random_phrase()
        self._clear()
        self.welcome()
        while self.missed < 5:
            self.active_phrase.display()
            print(
                f"\nYou have {5 - self.missed} incorrect "
                f"{self._plural(5 - self.missed)} left.")
            guess = self.get_guess()
            self.guesses.append(guess)
            self._clear()
            if self.active_phrase.check_letter(guess):
                print(f"Yes!  The letter “{guess}” is in the phrase!")
            else:
                print(f"Darn!  The letter “{guess}” isn't in the phrase.")
                self.missed += 1
            if self.active_phrase.check_complete():
                break
        # The else block executes if the player runs out of incorrect guesses.
        else:
            self.game_over(False)
            if not self._play_again():
                # The game object will be destroyed immediately upon returning
                # to the main loop, so call the goodbye method now.
                self._goodbye()
                return False
            return True
        # This executes if the player guesses all the letters in the phrase.
        self.game_over(True)
        if not self._play_again():
            self._goodbye()
            return False
        return True

    def get_random_phrase(self):
        """Randomly selects a phrase to use in the game.

        Arguments:  None.

        Returns:
        A phrase object.
        """
        return self.phrases[random.randint(0, 4)]

    def welcome(self):
        """Prints a welcome message.

        Arguments:  None.

        Returns:  Nothing.
        """
        print("=" * 40)
        print("Welcome to Phrase Hunter")
        print("\nA Treehouse Python Techdegree Project")
        print("\nby Steven Tagawa")
        print("=" * 40)
        return

    def get_guess(self):
        """Gets a letter from the player.

        Arguments:  None.

        Returns:  A valid guess from the player.
        """
        while True:
            response = input("\nGuess a letter:  ").lower()
            if self._valid_guess(response, self.guesses):
                break
        return response

    def game_over(self, won):
        """Prints a message after the game ends.

        Arguments:
        won -- True or False, depending on whether or not the player won.

        Returns:  Nothing.
        """
        if won:
            self.active_phrase.display()
            print("\nCongratulations!  You guessed the phrase.")
        else:
            print("\nOh no!  You ran out of incorrect guesses.")
            print(f"The phrase was “{self.active_phrase}.”")
        return

    def _valid_guess(self, response, guessed):
        """Validates the player's input.

        Arguments:
        response -- The player's input (already converted to lower-case).
        guessed -- A list of letters already guessed.

        Returns:
        True if the input is valid; otherwise False.
        """
        if len(response) == "":
            print("You didn't guess anything!  Try again.")
            return False
        elif len(response) > 1:
            print("One letter at a time, please!  Try again.")
            return False
        elif ord(response) not in range(97, 123):
            print("That's not a letter!  Try again.")
            return False
        elif response in guessed:
            print("You already guessed that letter!  Try again.")
            return False
        return True

    def _clear(self):
        """Clears the screen (sometimes)."""
        # Print a visual cue that the screen should clear for terminal emulators
        # that do not recognize the system call.  (For those that do, the cue
        # will instantly disappear.)
        print(">"*30, "CLEAR SCREEN", "<"*30)
        os.system("cls" if "name" == "nt" else "clear")

    def _goodbye(self):
        """Prints a goodbye message.

        Arguments:  None.

        Returns:  Nothing.
        """
        print("\n" + "=" * 40)
        print("Thanks for playing!  See you again soon!")
        print("=" * 40 + "\n")
        return

    def _plural(self, number):
        if number == 1:
            return "guess"
        return "guesses"

    def _play_again(self):
        """Asks the player if they would like to play again.

        Arguments:  None.

        Returns:
        True if the player wants to play again; otherwise False.
        """
        response = ""
        while response.lower() != "y":
            response = input("\nDo you want to play again? [Y/N]  ")
            if not self._check_yes_no(response):
                continue
            if response.lower() == "n":
                return False
        return True

    def _check_yes_no(self, string):
        """Checks the validity of a response to a yes/no prompt.

        Arguments:
        string -- the response to check.

        Returns:
        True if the response is valid; otherwise False.
        """
        if string.lower() not in ["y", "n"]:
            print("Sorry, I need a 'y' or an 'n' here...  Try again.")
            return False
        return True
