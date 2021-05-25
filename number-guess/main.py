import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Please guess a number between one and {x}: '))
        print(guess)

guess(10)