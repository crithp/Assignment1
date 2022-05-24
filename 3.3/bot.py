"""
    Test cases:
        I am hungry
        Are you skilled at robbing banks?
        Do you have any idea how large dogs are?
        I think John is silly
        I think John is very silly
        I hope you have a great day!
        Have an average day
"""

import re


def response(text):
    substitutions = [
        (r".*[i|I] am ([A-z]+).*?", r"Hello '\1' I am Bob the Bot"),
        (r".*[a|A]re you skilled at ([A-z\s]+)\?", r"I am very skilled at \1"),
        (r".*[h|H]ow ([A-z]+) ([A-z]+) are\?", r"\2 are very \1"),
        (r".*[i|I] think ([A-z]+) is((?:\svery)*) ([A-z]+)", r"I agree that \1 is\2 \3"),
        (r".*[h|H]ave a(n*) ([A-z]+) day!*", r"You have a\1 \2 day too!"),
    ]

    for find, replace in substitutions:
        if re.match(find, text):
            return re.sub(find, replace, text)

    return "I did not understand you"


if __name__ == '__main__':
    while True:
        text = input("You: \t\t\t")
        print("Bob the Bot: \t" + response(text))
