import random
from words import words

# print(words)

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word

def hangman():
    word = get_valid_word(words)

user_input = input('type something hear:')
print(user_input)