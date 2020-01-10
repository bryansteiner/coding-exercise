import string
import random


def getMissingLetters(sentence=""):             # default argument: empty string --> should return "abcdef...xyz"

    alphabet = set(string.ascii_lowercase)      # set contains every letter of the alphabet
    appears = set()                             # set will hold unique letters we find in the sentence

    for x in sentence:
        if x.isalpha():                         # first check if x is even a letter
            appears.add(x.lower())              # only add lowercase letters to set
            if len(appears) == 26: break        # check if we've exhausted all possible letters

    solution = alphabet - appears               # set difference to get letters that don't appear at all in sentence

    solution = ''.join(sorted(solution))        # convert solution set to a sorted string
    return solution


# Test cases:
print(getMissingLetters("A quick brown fox jumps over the lazy dog"))
print(getMissingLetters())
print(getMissingLetters(''.join(random.choices(string.ascii_letters + string.digits + string.whitespace, k=100000000000))))
