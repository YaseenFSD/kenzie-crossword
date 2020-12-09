#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Crossword Solver Program"""

__author__ = "Yaseen Al-Salamy"

import re


def find_words(word, list_source):
    """Input word with spaces as unknown && returns list of possible matches"""
    re_pattern = re.compile(r"^{}$".format(word.replace(" ", r"\w")))
    return filter(re_pattern.match, list_source)
    # YOUR HELPER FUNCTION GOES HERE


def main():
    with open('dictionary.txt') as f:
        words = f.read().split()
    test_word = input("""Please enter a word to solve.\nUse spaces to signify unknown letters:
""").lower()
    # YOUR ADDITIONAL CODE HERE
    print("Possible outcomes:")
    for word in find_words(test_word, words):
        print(word)
    # print(find_words(test_word, words))


if __name__ == '__main__':
    main()
