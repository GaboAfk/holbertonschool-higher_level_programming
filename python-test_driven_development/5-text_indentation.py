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
    phrase = ""
    space = 0
    for letter in text:
        if space:
            space = 0
            if letter == " ":
                continue
        phrase += letter
        if letter == "." or letter == "?" or letter == ":":
            print(phrase)
            print()
            phrase = ""
            space = 1
    print(phrase, end="")
