from pathlib import Path
# importing the lists of words
words_4 = Path("wordlists/4_letter_words.txt").read_text(encoding="utf-8").splitlines()
words_5 = Path("wordlists/5_letter_words.txt").read_text(encoding="utf-8").splitlines()
words_6 = Path("wordlists/6_letter_words.txt").read_text(encoding="utf-8").splitlines()

import random
# picks one random word from list NAME and converts it into uppercase
target_word_4 = random.choice(words_4).upper()
target_word_5 = random.choice(words_5).upper()
target_word_6 = random.choice(words_6).upper()

# test that the import works correctly
print("Random 4-letter word:", target_word_4)
print("Random 5-letter word:", target_word_5)
print("Random 6-letter word:", target_word_6)