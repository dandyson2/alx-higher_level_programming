#!/usr/bin/python3
"""The module contains a function that prints 2 new lines after ".?:" character

"""


def text_indentation(text):
    """Print the text with 2 new lines after ".?:" characters.

    Args:
        text (str): The input string.

    Returns:
        None

    Raises:
        TypeError: If text is not a string.

    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    s = text[:]

    for d in ".?:":
        list_text = s.split(d)
        s = ""
        for i in list_text:
            i = i.strip(" ")
            s = i + d if s == "" else s + "\n\n" + i + d

    print(s[:-3], end="")
