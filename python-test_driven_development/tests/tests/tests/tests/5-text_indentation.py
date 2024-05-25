#!/usr/bin/python3
"""
This module provides a function `text_indentation`\
that prints a text with 2 new lines after each of \
these characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The text to be printed

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_characters = {'.', '?', ':'}
    i = 0
    while i in range(len(text)):
        if text[i] in special_characters:
            print(f"{text[i]}\n\n", end="")
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
        else:
            print(text[i], end="")
            i += 1


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
