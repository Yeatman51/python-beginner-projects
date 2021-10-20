import random
from words import words

# print(words)

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
   word = get_valid_word(words)
   word_letters = set(words)
   alphabet = set(string.ascii_uppercase)
   used_letters = set() 

   # getting user input
   user_letter = input('Guess a letter: ').upper()
   if user_letter in alphabet - used_letters:
      used_letters.add(user_letter)
      if user_letter in word_letters:
         word_letters.remove(user_letter)

   elif user_letter in used_letters:
      print('do you have already used that character. \n please try again.')

   else:
      print('Invalid Character. \n please try again')

user_input = input('type something hear:')
print(user_input)