from src.wordle import Wordle
from termcolor import colored
import random

file_dir = "src/data/words_freq.txt"
wordle = Wordle(file_dir)
wordle.run()

