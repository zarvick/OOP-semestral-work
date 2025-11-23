# this program contains games implementaiton main logic

class game():

    def __init__(self):
        self.words = self.load_words()
        self.random_word = None

    def load_words(self):
        # abstract method, implementation of this method is in children classes
        return []

    def choose_word(self):
        import random # built-in class that can pick random thing from a parameter depending on its data type
        self.random_word = random.choice(self.words).upper() # .upper() converts the words into uppercase
        return self.random_word

    def try_word(self, word): # method that checks that the word has right length compared to choosen 4,5,6 letter game
        word = word.upper() # .upper() converts the words into uppercase
        if len(word) != self.word_length():
            raise ValueError(f"Word must be {self.word_length()} letters long") # if the condition is not TRUE than prints this error
        return word

    def split_words(self, word):
        return list(word.upper()) # built-in class that separates letter from word and puts one letter on one index of a list + converts the word into uppercase

    def compare_words(self, guess):
        guess = self.try_word(guess) # definiton of new parameter
        target = self.random_word.upper() # same thing for target word
        result = [] # empty list where after for cycle are printed colors based on the conditions

        for i, letter in enumerate(guess):
            if letter == target[i]: # when the letter and its position in guess word matches target word
                result.append("green")
            elif letter in target: # if the letter in guess word is somewhere used in target word, so correct letter but not position
                result.append("yellow")
            else: # letter which is in guess word but not present in target word
                result.append("grey")

        return result # returns the result of this cycle into the list: result = []


    def evaluate_guess():
        pass

    def reset():
        pass

class game_4letter(game):

    def __init__(self):
        super().__init__()

    def load_words(self):
        from pathlib import Path
        self.choosen_word = Path("wordlists/4_letter_words.txt").read_text(encoding="utf-8").splitlines()
        return self.choosen_word

    def word_length(self):
        return 4

    def max_attempts():
        pass

class game_5letter(game):

    def __init__(self):
        super().__init__()

    def load_words(self):
        from pathlib import Path
        self.choosen_word = Path("wordlists/5_letter_words.txt").read_text(encoding="utf-8").splitlines()
        return self.choosen_word

    def word_length(self):
        return 5
    
    def max_attempts():
        pass

class game_6letter(game):

    def __init__(self):
        super().__init__()

    def load_words(self):
        from pathlib import Path
        self.choosen_word = Path("wordlists/6_letter_words.txt").read_text(encoding="utf-8").splitlines()
        return self.choosen_word

    def word_length(self):
        return 6

    def max_attempts():
        pass


# test that the import works correctly
game4 = game_4letter()
game5 = game_5letter()
game6 = game_6letter()
print("Random 4-letter word:", game4.choose_word())
print("Random 5-letter word:", game5.choose_word())
print("Random 6-letter word:", game6.choose_word())

# test that length of the word is correct/incorrect
game4.try_word("test")    # správná délka
# game4.try_word("hello")   # špatná délka → mělo by vyhodit ValueError
game5.try_word("hello")   # správná délka
# game5.try_word("test")    # špatná délka → mělo by vyhodit ValueError
game6.try_word("rabbit")  # správná délka

# test for letters separation and comparison with random choosen word
print("4-letter word:", game4.split_words("test") )
test_guess = "test"

print("Chosen word (4-letter):", game4.random_word)
print("Your guess:", test_guess)
print("Comparison result:", game4.compare_words(test_guess))
# doesnt work if the same letter is used more than once !!!!