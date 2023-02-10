import random

from src.utils import print_error, print_success, print_warning, print_wrong_p

random.seed(42)

class Wordle:
    def __init__(self, file_dir : str, word_len : int = 5, limit : int = 10_000):
        self.word_len = word_len
        self.words = self.generate_word_freq(file_dir, word_len, limit)

# Build Data

    def generate_word_freq(self, file_dir, word_len : int, limit : int):
        # Build Data
        w_freq = {}
        with open(file_dir) as f:
            for line in f:
                word, freq = line.split(",")
                if len(word) == self.word_len:
                    w_freq[word] = int(freq)

        # Sort Data
        sort_w_freq = sorted(w_freq.items(), key=lambda x : x[1], reverse=True)

        # Drop Frequency
        words = [item[0].upper() for item in sort_w_freq[:limit]]

        return words

    def check_word(self, word, guess):

        for char_, g_char in zip(word, guess):
            if char_ == g_char :
                print_success(f' {g_char} ', end=' ')
                    # print(' ', end='')
            elif g_char in word:
                print_wrong_p(f' {g_char} ', end=' ')
                    # print(' ', end='')
            else:
                print_error(f' {g_char} ', end=' ')
                    # print(' ', end='')
        print()

    def run(self):
        # Random Word
        word = random.choices(self.words)[0]

        # Start Game
        n_guess = 6
        chance = False
        for i in range(n_guess):
            guess = input(f"Guess a {self.word_len} word letter or press q to quit the game : ")
            if guess == 'q':
                break
            guess = guess.upper()

            # Word Length
            if len(guess) != self.word_len:
                print(f"Enter a {self.word_len} letter word. You enter {len(guess)}")
                continue

            #Check Valid Word
            elif guess not in self.words:
                print_error("This word has not defined")
                continue

            # Check Guess
            if guess == word:
                print_success(f' {word} ')
                print_success(f"You Win")
                chance = True
                break

            # Check Valid, Invalid Position, Invalid Character
            self.check_word(word, guess)


        if not chance:
            print_warning(f"OOOOOps Game Over!!!!! The right world is {word}")


