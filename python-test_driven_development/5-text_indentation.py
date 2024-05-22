#!/usr/bin/python3
"""text_indentation module
"""


def text_indentation(text):
    """function that prints a text with 2 new
    lines after each of these characters: ., ? and :

    Args:
        text (str): text to print

    Raises:
        TypeError: only str type accepted
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    delimiters = (".", "?", ":")
    phrase = ""
    for letter in text:
        phrase += letter
        if letter in delimiters:
            print(phrase.strip())
            print()
            phrase = ""
    if phrase:
        print(phrase.strip(), end="")
