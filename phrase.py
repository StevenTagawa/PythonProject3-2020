"""This module contains the Phrase class for the Phrase Hunter game."""


class Phrase:
    """Class holding the phrase used in the Phrase Hunter game.

    Attributes:
    phrase -- The phrase itself.
    phrase_set -- The set of letters in the phrase.

    Public Methods:
    display() -- Prints the phrase (partially or fully revealed).
    check_letter() -- Checks a letter against the phrase.
    check_complete() -- Checks to see if the phrase is completely revealed.
    """

    def __init__(self, phrase):
        self.phrase = phrase
        self.phrase_set = set(list(self.phrase))
        self.phrase_set.remove(" ")

    def display(self):
        """Displays a partially or completely revealed phrase.

        Arguments:  None.

        Returns:  Nothing.
        """
        # More efficient than building a string one letter at a time...
        display_list = []
        for letter in self.phrase:
            # Replace letters not guessed with underscores.
            if letter in self.phrase_set:
                display_list.append("_")
            else:
                display_list.append(letter)
        # Extra space between letters.
        print("\n"+" ".join(display_list))
        return

    def check_letter(self, letter):
        """Checks a letter against the phrase.

        Arguments:
        letter -- The letter to check.

        Returns:
        True if the letter is in the phrase; False if it is not.
        """
        # If the letter is in the set of unguessed letters, take it out.
        if letter in self.phrase:
            self.phrase_set.remove(letter)
            return True
        return False

    def check_complete(self):
        """Checks if the phrase has been completely revealed.

        Arguments:  None.

        Returns:
        True if the phrase has been completely revealed; otherwise False.
        """
        # If there are no more unguessed letters, the set will be empty (False).
        return not self.phrase_set
