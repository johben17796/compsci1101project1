"""
Helper class for CSCI1101 Quiz Project
By Garrett
source for Self module:
https://www.geeksforgeeks.org/python/self-type-in-python/
"""

from typing import Self

class DisplayBox:
    """
    A display box which can have text added to it and easily printed out. All
    formatting is handled by the object itself.

    Example usage:
        >>> print(DisplayBox("Here is some sample text!", width=37))
        +-----------------------------------+
        |     Here is some sample text!     |
        +-----------------------------------+
    """

    def __init__(self, text: str = None, width: int = 66):
        self.text: list[str] = []
        self.width: int = width
        if text is not None:
            self.add_text(text)

    def __str__(self):
        output: list[str] = self.separator()
        for line in self.text:
            output += line
        output += self.separator()
        return output

    def separator(self) -> str:
        """
        Generates a separator based on the DisplayBox's width.

        Returns
        -------
        str
            _The separator generated_
        """
        return f"+{"-" * (self.width - 2)}+\n"

    def add_separator(self) -> Self:
        """
        Adds a separator line to the DisplayBox's text.

        Returns Self
        -------
        """
        self.text.append(self.separator())
        return self

    def add_text(self, *lines) -> Self:
        """
        Adds all supplied lines to the DisplayBox's text, automatically formatting
        them in the process. All provided parameters must be representable as strings.

        Returns Self
        -------
        """
        for line in lines:
            # The amount of padding required on both sides of text in order to reach width
            spaces: int = (self.width - (len(line) + 2)) // 2
            # A situation where width is even while len(text) is odd or vice versa causes the line
            # to be 1 character smaller than intended, so we add an extra space to compensate
            if self.width % 2 != len(line) % 2:
                self.text.append(f"|{" " * (spaces + 1)}{line}{" " * spaces}|\n")
            else:
                self.text.append(f"|{" " * spaces}{line}{" " * spaces}|\n")
        return self
