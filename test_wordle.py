# program with basic tests of implemented methods from game.py, tests are done with use of pytest
# to run this test use command in terminal: python -m pytest -v test_wordle.py

# import of classes from game.py
from game import game_4letter, game_5letter, game_6letter


# tests of method try_word
def test_try_word_length():
    game4 = game_4letter()
    game4.random_word = "WORD"
    assert game4.try_word("WORD") == "WORD"
    assert game4.try_word("WORDS") is None

    game5 = game_5letter()
    game5.random_word = "APPLE"
    assert game5.try_word("APPLE") == "APPLE"
    assert game5.try_word("APP") is None

    game6 = game_6letter()
    game6.random_word = "TUNNEL"
    assert game6.try_word("TUNNEL") == "TUNNEL"
    assert game6.try_word("TUNNE") is None


# tests of method compare_words but with no letter duplicates
def test_compare_words_no_duplicates():
    game4 = game_4letter()
    game4.random_word = "WORD"
    result = game4.compare_words("WOOD")
    assert result == ["green", "green", "grey", "green"]

# tests of method compare_words but with letter duplicates
def test_compare_words_with_duplicates():
    game6 = game_6letter()
    game6.random_word = "TUNNEL"
    result = game6.compare_words("NNNNNN")
    assert result == ["grey", "grey", "green", "green", "grey", "grey"]

# test of method evaluate_guess, target word = guess
def test_evaluate_guess_win():
    game4 = game_4letter()
    game4.random_word = "TEST"
    status, colors = game4.evaluate_guess("TEST")
    assert status == "win"
    assert colors == ["green", "green", "green", "green"]

# test of method evaluate_guess, running out of attempts
def test_evaluate_guess_lose():
    game4 = game_4letter()
    game4.random_word = "TEST"
    game4.attempts_left = 1
    status, colors = game4.evaluate_guess("FAIL")
    assert status == "lose"
    assert colors == ["grey", "grey", "grey", "grey"]

# test of method evaluate_guess, game in progress
def test_evaluate_guess_partial():
    game5 = game_5letter()
    game5.random_word = "APPLE"
    status, colors = game5.evaluate_guess("ALERT")
    assert status == "continue"
    assert colors == ["green", "yellow", "yellow", "grey", "grey"]

# test of method split_words
def test_split_words():
    game4 = game_4letter()
    assert game4.split_words("WORD") == ["W","O","R","D"]

    game5 = game_5letter()
    assert game5.split_words("APPLE") == ["A","P","P","L","E"]

    game6 = game_6letter()
    assert game6.split_words("TUNNEL") == ["T","U","N","N","E","L"]
