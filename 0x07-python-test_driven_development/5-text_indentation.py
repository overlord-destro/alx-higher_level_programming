#!/usr/bin/python3
"""Function to  print text with 2 new lines after certain characters"""


def text_indentation(text):
    """
    Function that prints 2 new lines after ['.', ':', '?'] and accepts
    only strings else will raise a type errorr
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new = ""
    for i in range(len(text)):
        if text[i] == " " and text[i - 1] in [".", ":", "?"]:
            continue
        else:
            new += text[i]

    for char in new:
        if char in [".", "?", ":"]:
            print(char + "\n\n", end="")
        else:
            print(char, end="")
