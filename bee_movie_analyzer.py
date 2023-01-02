"""Script to analyze a text file of 'the bee movie' movie script"""

import re  # you can use this module for a one line replacement of all punctuation
from typing import Dict


def nth_most_common_words(path: str, n: int):
    """The nth_most_common_words function takes the path to the script file and the
    word frequency rank and returns a list of words at that rank
    return an empty string if the rank is below 1 or if the rank does not exist

    Args:
        path (str): The path to the script file to analyze
        n (int): the rank of the word list returned

    Returns:
        List: a list of all the words at rank n"""
    words = get_words(path)
    word_counts = count_words(words)

    words_by_count: Dict[int, list] = {}
    for word, count in word_counts.items():
        if count in words_by_count:
            words_by_count[count].append(word)
        else:
            words_by_count[count] = [word]

    ranks = list(words_by_count)
    ranks.sort(reverse=True)

    if n > len(ranks) or n == 0:
        return []

    return words_by_count[ranks[n - 1]]


def count_words(word_list: list) -> dict:
    """The count_words function takes a word list and returns a dictionary with
    the word as key and the value is the word count for that word"""
    word_counts: Dict[str, int] = {}
    for word in word_list:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts


def get_words(path):
    """The get_words function takes a file path and returns a filtered list of
    the words in the file.
    The words should all be lowercase
    It filters out all the punctuation except contractions (they count as their own words)."""
    words = []
    for line in open(
        path
    ):  # loop through every line in the file. path should be a string
        words.extend(
            re.sub(r'[,.?!"\-:]', "", line).lower().split()
        )  # of the file path to the script.
    return words


def word_probability(path, word):
    """The word probability function takes a file path and a word and returns a float
    that is a decimal value of the probability that any single word in the script
    would be that word.
    If the word is not in the script, the probability is 0"""
    words = get_words(path)
    word_counts = count_words(words)

    if word in words:
        return word_counts[word] / len(words)
    else:
        return 0


if __name__ == "__main__":
    # For extra practice, this would be a fun place to put a menu to access script stats
    # path = input("path: ")
    # n = int(input("n: "))
    # word = input("word: ")

    path = "test.txt"
    n = 3
    word = "the"

    for n in range(50):
        print(nth_most_common_words(path, n))

    prob = word_probability(path, word)
    print(prob)
