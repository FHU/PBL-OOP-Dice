"""Tests to make sure the bee movie analyzer correctly analyzes text files. Uses the script as input.
"""

from pytest import approx, mark

import bee_movie_analyzer


@mark.parametrize("test_word", ["buzz", "you", "barry", "you'll"])
def test_get_words(test_word):
    """Check that get_words returns a list that includes some of the correct words"""
    words = bee_movie_analyzer.get_words("test.txt")

    assert test_word in words


@mark.parametrize(
    "test_word", ["jesus", "Barry", "fly.", "great!", "right?", "so,", '"you', "-"]
)
def test_get_words_missing(test_word):
    """Check that get_words returns a list that does not include some words"""
    words = bee_movie_analyzer.get_words("test.txt")

    assert test_word not in words


@mark.parametrize(
    "test_word, count", [("one", 1), ("two", 2), ("three", 3), ("four", 4)]
)
def test_count_words(test_word, count):
    """Check that count_words, givin a list of words, counts them appropriatly"""
    words = [
        "one",
        "two",
        "two",
        "three",
        "three",
        "three",
        "four",
        "four",
        "four",
        "four",
    ]
    word_counts = bee_movie_analyzer.count_words(words)
    assert word_counts[test_word] == count


def test_count_words_nothing_extra():
    """Check that count_words does not include words not in the list passed to it"""
    words = [
        "one",
        "two",
        "two",
        "three",
        "three",
        "three",
        "four",
        "four",
        "four",
        "four",
    ]
    word_counts = bee_movie_analyzer.count_words(words)
    assert set(words) == set(word_counts.keys())


@mark.parametrize(
    "rank, word_list",
    [
        (1, ["you"]),
        (2, ["the"]),
        (3, ["a"]),
        (4, ["i"]),
        (46, ["yeah", "could"]),
        (100, []),
        (0, []),
    ],
)
def test_nth_most_common_words(rank, word_list):
    """Check that a few word ranks are accurate in nth_most_common_words"""
    assert bee_movie_analyzer.nth_most_common_words("test.txt", rank) == word_list


@mark.parametrize(
    "word, prob",
    [("i", 0.02610595303113053), ("buzz", 0.0014199890770070999), ("jesus", 0)],
)
def test_word_probability(word, prob):
    """Check that a few word probabilities are accurate in word_probability"""
    assert bee_movie_analyzer.word_probability("test.txt", word) == approx(prob)
